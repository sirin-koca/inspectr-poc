package inspectr

# InspectR PoC Policy-as-Code for the Trondheim Kommune MUNDAT use case.
# These rules check structural and declared design-time evidence in the
# pipeline blueprint. They do not determine legal compliance.

import rego.v1

nodes := object.get(
    object.get(input, "pipeline", {}),
    "nodes",
    []
)

required_stages := {
    "tk_request_intake",
    "validate_request",
    "retrieve_relevant_data",
    "process_data_for_compliance",
    "run_compliance_checks",
    "prepare_sharing_decision",
    "tk_decision_output"
}

node_labels := {node.label | some node in nodes}
missing_stages := required_stages - node_labels

connections := object.get(
    object.get(input, "pipeline", {}),
    "connections",
    []
)

node_labels_by_id := {node.id: node.label | some node in nodes}

actual_edges := {
    sprintf("%s>%s", [
        node_labels_by_id[edge.from.node],
        node_labels_by_id[edge.to.node]
    ]) |
    some edge in connections
}

expected_edges := {
    "tk_request_intake>validate_request",
    "validate_request>retrieve_relevant_data",
    "retrieve_relevant_data>process_data_for_compliance",
    "process_data_for_compliance>run_compliance_checks",
    "run_compliance_checks>prepare_sharing_decision",
    "prepare_sharing_decision>tk_decision_output"
}

flow_valid if {
    count(nodes) == count(required_stages)
    count(missing_stages) == 0
    actual_edges == expected_edges
}

article_structure := {
    "rule": "TK-STRUCT-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT pipeline structure",
    "reason": "The blueprint does not contain the required TK compliance-flow stages and connections.",
    "evidence": {
        "missing_stages": missing_stages,
        "observed_stages": [node.label | some node in nodes],
        "observed_edges": actual_edges
    },
    "remedy": "Add the missing TK stages and connect them in the documented intake-to-output order."
} if {
    count(missing_stages) > 0
} else := {
    "rule": "TK-STRUCT-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT pipeline structure",
    "reason": "The blueprint contains the required stages, but not in the documented order.",
    "evidence": {
        "missing_stages": [],
        "observed_stages": [node.label | some node in nodes],
        "observed_edges": actual_edges
    },
    "remedy": "Connect the TK stages in the documented intake-to-output order."
} if {
    count(missing_stages) == 0
    not flow_valid
} else := {
    "rule": "TK-STRUCT-01",
    "status": "OK",
    "legal_reference": "MUNDAT pipeline structure",
    "reason": "The blueprint contains the seven documented TK compliance-flow stages and connections.",
    "evidence": {
        "stages_checked": count(nodes)
    },
    "remedy": null
} if {
    count(missing_stages) == 0
    flow_valid
}

logging_failures contains node.label if {
    some node in nodes
    object.get(object.get(node, "compliance_extensions", {}), "has_logging", false) != true
}

article_traceability := {
    "rule": "TK-TRACE-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT logging and traceability requirement",
    "reason": "One or more pipeline stages do not declare logging capability.",
    "evidence": {
        "nodes_without_logging": logging_failures
    },
    "remedy": "Declare logging capability for every pipeline stage and retain traceability of the request, data access, checks, and decision."
} if {
    count(logging_failures) > 0
} else := {
    "rule": "TK-TRACE-01",
    "status": "OK",
    "legal_reference": "MUNDAT logging and traceability requirement",
    "reason": "All pipeline stages declare design-time logging capability.",
    "evidence": {
        "nodes_checked": count(nodes)
    },
    "remedy": null
}

data_source_nodes contains node if {
    some node in nodes
    node.kind == "source"
}

invalid_sources contains node.label if {
    some node in data_source_nodes
    ext := object.get(node, "compliance_extensions", {})
    object.get(ext, "source_id", "") == ""
}

invalid_sources contains node.label if {
    some node in data_source_nodes
    ext := object.get(node, "compliance_extensions", {})
    object.get(ext, "approved_source", false) != true
}

article_data_provenance := {
    "rule": "TK-DATA-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT data-source and provenance requirement",
    "reason": "A pipeline data source lacks a source identifier or is not marked as approved.",
    "evidence": {
        "invalid_sources": invalid_sources
    },
    "remedy": "Declare the source identifier and approval status for each data-source node."
} if {
    count(invalid_sources) > 0
} else := {
    "rule": "TK-DATA-01",
    "status": "OK",
    "legal_reference": "MUNDAT data-source and provenance requirement",
    "reason": "Pipeline data sources provide declared provenance and approval evidence.",
    "evidence": {
        "data_sources_checked": count(data_source_nodes)
    },
    "remedy": null
}

risk_check_nodes contains node.label if {
    some node in nodes
    node.label == "run_compliance_checks"
}

article_risk := {
    "rule": "TK-RISK-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT DPIA and risk-assessment requirement",
    "reason": "The blueprint does not contain a dedicated compliance and risk-assessment stage.",
    "evidence": {
        "risk_check_stage": "run_compliance_checks"
    },
    "remedy": "Add a stage that performs the documented compliance, DPIA, and risk checks."
} if {
    count(risk_check_nodes) == 0
} else := {
    "rule": "TK-RISK-01",
    "status": "OK",
    "legal_reference": "MUNDAT DPIA and risk-assessment requirement",
    "reason": "The blueprint contains a dedicated compliance and risk-assessment stage.",
    "evidence": {
        "risk_check_stage": risk_check_nodes
    },
    "remedy": null
}

decision_nodes contains node if {
    some node in nodes
    node.label == "prepare_sharing_decision"
}

missing_human_review contains node.label if {
    some node in decision_nodes
    ext := object.get(node, "compliance_extensions", {})
    object.get(ext, "human_oversight", null) == null
}

disabled_human_review contains node.label if {
    some node in decision_nodes
    ext := object.get(node, "compliance_extensions", {})
    object.get(ext, "human_oversight", null) == false
}

article_human_review := {
    "rule": "TK-HUMAN-01",
    "status": "FAIL",
    "legal_reference": "MUNDAT sharing-decision review requirement",
    "reason": "The sharing decision stage explicitly disables human review.",
    "evidence": {
        "components_without_human_review": disabled_human_review
    },
    "remedy": "Provide a human approval or override step before sharing data."
} if {
    count(disabled_human_review) > 0
} else := {
    "rule": "TK-HUMAN-01",
    "status": "HUMAN",
    "legal_reference": "MUNDAT sharing-decision review requirement",
    "reason": "The blueprint contains a sharing decision stage but does not provide explicit human-review evidence.",
    "evidence": {
        "components_requiring_review": missing_human_review
    },
    "remedy": "Declare human review or an override checkpoint before sharing data."
} if {
    count(disabled_human_review) == 0
    count(missing_human_review) > 0
} else := {
    "rule": "TK-HUMAN-01",
    "status": "OK",
    "legal_reference": "MUNDAT sharing-decision review requirement",
    "reason": "The sharing decision stage explicitly represents human review evidence.",
    "evidence": {
        "decision_stages_checked": count(decision_nodes)
    },
    "remedy": null
} if {
    count(disabled_human_review) == 0
    count(missing_human_review) == 0
}

results := [
    article_structure,
    article_data_provenance,
    article_traceability,
    article_risk,
    article_human_review
]

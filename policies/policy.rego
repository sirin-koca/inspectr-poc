package inspectr

#
# InspectR PoC Policy-as-Code
# EU AI Act subset:
#   Article 10 — Data and data governance
#   Article 12 — Record-keeping
#   Article 14 — Human oversight
#

import rego.v1


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

nodes := object.get(
    object.get(input, "pipeline", {}),
    "nodes",
    []
)


# ---------------------------------------------------------
# AIA-12 — RECORD-KEEPING / LOGGING
#
# PoC interpretation:
# Every pipeline node must explicitly declare has_logging=true.
# ---------------------------------------------------------

logging_failures contains node.label if {
    some node in nodes
    object.get(
        object.get(node, "compliance_extensions", {}),
        "has_logging",
        false
    ) != true
}

article_12 := {
    "rule": "AIA-12",
    "status": "FAIL",
    "legal_reference": "EU AI Act Article 12 — Record-keeping",
    "reason": "One or more pipeline components do not provide evidence of automatic logging capability.",
    "evidence": {
        "nodes_without_logging": logging_failures
    },
    "remedy": "Add explicit logging capability to the identified pipeline components."
} if {
    count(logging_failures) > 0
} else := {
    "rule": "AIA-12",
    "status": "OK",
    "legal_reference": "EU AI Act Article 12 — Record-keeping",
    "reason": "All pipeline components provide design-time evidence of logging capability.",
    "evidence": {
        "nodes_checked": count(nodes)
    },
    "remedy": null
}


# ---------------------------------------------------------
# AIA-10 — DATA GOVERNANCE / PROVENANCE
#
# PoC operationalisation:
# Data-source nodes must identify their provenance and
# the source must be explicitly approved.
# ---------------------------------------------------------

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

article_10 := {
    "rule": "AIA-10",
    "status": "FAIL",
    "legal_reference": "EU AI Act Article 10 — Data and data governance",
    "reason": "A pipeline data source lacks required provenance information or is not marked as an approved source.",
    "evidence": {
        "invalid_sources": invalid_sources
    },
    "remedy": "Provide a source identifier and verify that the data source belongs to the approved municipal source set."
} if {
    count(invalid_sources) > 0
} else := {
    "rule": "AIA-10",
    "status": "OK",
    "legal_reference": "EU AI Act Article 10 — Data and data governance",
    "reason": "Pipeline data sources provide provenance information and are marked as approved.",
    "evidence": {
        "data_sources_checked": count(data_source_nodes)
    },
    "remedy": null
}


# ---------------------------------------------------------
# AIA-14 — HUMAN OVERSIGHT
#
# PoC boundary:
# If an automated decision-support component exists,
# explicit human-oversight evidence must also exist.
#
# Missing evidence -> HUMAN rather than FAIL.
# ---------------------------------------------------------

decision_nodes contains node if {
    some node in nodes

    ext := object.get(node, "compliance_extensions", {})

    object.get(ext, "automated_decision_support", false) == true
}

missing_human_oversight contains node.label if {
    some node in decision_nodes

    ext := object.get(node, "compliance_extensions", {})

    object.get(ext, "human_oversight", false) != true
}

article_14 := {
    "rule": "AIA-14",
    "status": "HUMAN",
    "legal_reference": "EU AI Act Article 14 — Human oversight",
    "reason": "Automated decision support is present, but the blueprint does not provide sufficient evidence of human oversight.",
    "evidence": {
        "components_requiring_review": missing_human_oversight
    },
    "remedy": "Define an explicit human-review or intervention checkpoint for the automated decision-support component."
} if {
    count(missing_human_oversight) > 0
} else := {
    "rule": "AIA-14",
    "status": "OK",
    "legal_reference": "EU AI Act Article 14 — Human oversight",
    "reason": "The blueprint explicitly represents human oversight for automated decision support.",
    "evidence": {
        "decision_components_checked": count(decision_nodes)
    },
    "remedy": null
}


# ---------------------------------------------------------
# InspectR result
# ---------------------------------------------------------

results := [
    article_10,
    article_12,
    article_14
]
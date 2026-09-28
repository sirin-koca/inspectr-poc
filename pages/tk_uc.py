import streamlit as st
# --------------------------------------------------
# TK COMPLIANCE FLOW
# --------------------------------------------------
st.markdown("### TK Compliance Flow")
st.write(
    """
    The Trondheim Kommune (TK) Use Case provides the application
        scenario used to demonstrate the InspectR PoC.
    The compliance flow defines the compliance-oriented process
    that forms the basis for the pipeline blueprint used in this PoC.
    """
)
st.image(
    "images/tk-uc-pl.jpg",
    caption="Trondheim Kommune Compliance Flow",
    width=900,
)
st.divider()
# --------------------------------------------------
# INLUMEN PIPELINE BLUEPRINT
# --------------------------------------------------

st.markdown("### inLUMEN Pipeline Blueprint")

st.write(
    """
    Based on the TK compliance flow, the pipeline blueprint below
    was created in inLUMEN. This blueprint represents the pipeline
    artifact subsequently provided to InspectR for compliance evaluation.
    """
)

st.image(
    "images/tk-uc-plbp.jpg",
    caption="TK Pipeline Blueprint created in inLUMEN",
    use_container_width=True,
)
    

st.title("TK Regulatory Sources and Scope")

st.write(
    "GDPR, the EU AI Act, and other governance sources are possible sources for the broader "
    "InspectR project. They are not evaluated directly by the current TK/MUNDAT PoC policy. "
    "A source requirement must first be interpreted for a context, mapped to required evidence, "
    "and then encoded as Policy-as-Code."
)

st.warning(
    "The active executable rules are TK/MUNDAT design-time checks. This page documents the boundary "
    "between regulatory source material and the current technical policy."
)

st.divider()
st.header("Active PoC rules")
st.markdown(
    """
| InspectR Rule | Requirement source | PoC focus | Blueprint evidence |
|---|---|---|---|
| `TK-STRUCT-01` | TK/MUNDAT pipeline design | Required stages and graph connections | `pipeline.nodes`, `pipeline.connections` |
| `TK-DATA-01` | TK/MUNDAT data-governance need | Source provenance and approval | `source_id`, `approved_source` |
| `TK-TRACE-01` | TK/MUNDAT traceability need | Stage logging declaration | `has_logging` |
| `TK-RISK-01` | TK/MUNDAT compliance process | Compliance and risk-check stage | `run_compliance_checks` |
| `TK-HUMAN-01` | TK/MUNDAT sharing governance | Human review before sharing | `human_oversight` |
"""
)

st.caption(
    "These are local operational interpretations for the TK/MUNDAT PoC. "
    "They do not establish full GDPR or EU AI Act conformity."
)

st.divider()
st.header("From source requirement to finding")
st.code(
    """Requirement or use-case need
        |
        v
Operational interpretation
        |
        v
Required evidence
        |
        v
Rego policy
        |
        v
Blueprint evidence
        |
        v
OPA evaluation
        |
        v
OK / FAIL / HUMAN""",
    language="text",
)

col1, col2, col3 = st.columns(3)

with col1:
    st.success("OK - evidence satisfies the encoded rule.")

with col2:
    st.error("FAIL - explicit evidence violates the encoded rule.")

with col3:
    st.warning("HUMAN - evidence is missing or ambiguous.")

st.info(
    "The future InspectR implementation can add legally mapped rule sets. "
    "This PoC first demonstrates the architecture and method with TK/MUNDAT requirements."
)

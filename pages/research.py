import streamlit as st

st.markdown("### Core Investigation")

st.info(
    """
    How can compliance requirements be operationalized and automatically evaluated 
    against data pipeline designs at design time?
    """
)

st.markdown("#### RQ1 — Design-Time Compliance")
st.write(
    """
    What compliance-relevant conclusions can be reliably derived from a
    static pipeline blueprint without access to runtime data or execution behaviour?
    """
)

st.markdown("#### RQ2 — Rule Codification")
st.write(
    """
    How can selected regulatory requirements be translated into machine-readable
    Policy-as-Code rules that can be evaluated against pipeline designs?
    """
)

st.markdown("#### RQ3 — Rule Applicability")
st.write(
    """
    How can InspectR determine which Policy-as-Code rules and compliance
    checkpoints are applicable to specific operations in a pipeline blueprint?
    """
)

st.markdown("#### RQ4 — Evidence Sufficiency")
st.write(
    """
    What design-time evidence must a pipeline blueprint provide for InspectR
    to evaluate an applicable rule, and how should insufficient evidence be handled?
    """
)

st.markdown("#### RQ5 — Blueprint Requirements")
st.write(
    """
    Which compliance-relevant information is already available in the inLUMEN
    blueprint, and what additional information must be explicitly represented
    to support reliable compliance inspection?
    """
)
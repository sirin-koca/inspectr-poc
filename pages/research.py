import streamlit as st

st.markdown("### Core Investigation")

st.info(
    """
    - How can regulation requirements, such as GDPR or AIA, can be operationalized and automatically evaluated 
    against data pipeline design blueprints at design time? 
    - What evidence must a pipeline specification expose so that a machine-executable policy can reach a justified compliance finding?
    """
)

st.markdown("#### Possible Research Questions")
st.write(
    """
    The InspectR PoC investigates the following research questions (RQs) in the context of
    the TK inLUMEN pipeline blueprint and a provisional subset of the EU AI Act (AIA):

    1. **RQ1 — Design-Time Compliance**: What compliance-relevant conclusions can be reliably derived from a static pipeline blueprint without access to runtime data or execution behaviour?
    2. **RQ2 — Rule Codification**: How can selected regulatory requirements be translated into machine-readable Policy-as-Code rules that can be evaluated against pipeline designs?
    3. **RQ3 — Rule Applicability**: How can InspectR determine which Policy-as-Code rules and compliance checkpoints are applicable to specific operations in a pipeline blueprint?
    4. **RQ4 — Evidence Sufficiency**: What design-time evidence must a pipeline blueprint provide for InspectR to evaluate an applicable rule, and how should insufficient evidence be handled?
    5. **RQ5 — Blueprint Requirements**: Which compliance-relevant information is already available in the inLUMEN blueprint, and what additional information must be explicitly represented to support reliable compliance inspection?
    """
)

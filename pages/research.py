import streamlit as st

st.title("Research")

st.info("""
    PROBLEM & METHOD:

    Core research problem: How do we translate contextual requirements into deterministic policy?
    PoC: Can this work directly on one TK/inLUMEN blueprint?
    Future architecture:How can the same method work across organizations and blueprint formats?
    IR:One mechanism for achieving that future generalization.
    "InspectR investigates the semantic gap between complex regulatory or governance "
    "requirements and deterministic software logic. The TK/MUNDAT pipeline is the concrete "
    "case used to test the architecture and Policy-as-Code method.
    """
)
st.markdown("#### Research Questions")
st.write(
    """
    1. **RQ1 — Design-Time Compliance**: What compliance-relevant conclusions can be reliably derived from a static pipeline blueprint without access to runtime data or execution behaviour?
    2. **RQ2 — Rule Codification**: How can selected regulatory requirements be translated into machine-readable Policy-as-Code rules that can be evaluated against pipeline designs?
    3. **RQ3 — Rule Applicability**: How can InspectR determine which Policy-as-Code rules and compliance checkpoints are applicable to specific operations in a pipeline blueprint?
    4. **RQ4 — Evidence Sufficiency**: What design-time evidence must a pipeline blueprint provide for InspectR to evaluate an applicable rule, and how should insufficient evidence be handled?
    5. **RQ5 — Blueprint Requirements**: Which compliance-relevant information is already available in the inLUMEN blueprint, and what additional information must be explicitly represented to support reliable compliance inspection?
    """
)

st.header("Contribution under investigation")
st.write(
    "InspectR demonstrates an architecture and operational method for translating selected "
    "regulatory and governance requirements into explainable Policy-as-Code checks over static data-pipeline blueprints."
)

st.header("Evidence for the claim")
st.markdown(
    """
    - Policy is separated from Python application logic.
    - OPA independently evaluates Rego against blueprint evidence.
    - Each rule exposes its interpretation, evidence, result, and remedy.
    - `OK`, `FAIL`, and `HUMAN` distinguish satisfied, negative, and insufficient evidence.
    - The same blueprint produces repeatable results.
    - Limitations and alternative interpretations are documented.
    """
)

st.warning(
    "Novelty is a research question, not an assumption. " \
    "OPA and Policy-as-Code are established technologies; "
    "the thesis must position the InspectR combination against " \
    "related work."
)



import streamlit as st

st.subheader("EU AI Act Subset")

st.write(
    """
    - The InspectR PoC will investigate a minimal subset of the EU Artificial
    Intelligence Act which are most suitable for the TK UC.     
    - The selected provisions 
    will be translated into machine-readable Policy-as-Code rules and evaluated against 
    the TK inLUMEN pipeline blueprint.
    - It is therefore crucial to build the pipeline artifact with sufficient information and identify 
    the most suitable and applicabple AIA subset in order to demonstrate InspectR's capabilities and 
    limitations in a meaningful way.
    - The purpose is to explore how selected legal requirements can be
    translated into machine-readable Policy-as-Code (PaC) rules and
    evaluated against information available in the TK pipeline blueprint.
    """
)
st.divider()

# --------------------------------------------------
# CANDIDATE AIA PROVISIONS
# --------------------------------------------------

st.markdown("### Candidate AIA Provisions - work-in-progress")

st.markdown(
    """
| Candidate Rule | AIA Provision | What the provision addresses |
|---|---|---|
| `AIA-5-1-B` | [Article 5(1)(b)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_5) | Exploitation of vulnerabilities related to age, disability, or a specific social or economic situation, under the conditions defined by the provision. |
| `AIA-5-1-C` | [Article 5(1)(c)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_5) | Evaluation or classification of persons resulting in prohibited social-scoring outcomes. |
| `AIA-5-1-G` | [Article 5(1)(g)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_5) | Biometric categorisation used to deduce or infer the sensitive characteristics specified by the provision, subject to its stated exclusions. |
"""
)

st.caption(
    "Legal source: Regulation (EU) 2024/1689 — Artificial Intelligence Act, EUR-Lex."
)

st.divider()

# --------------------------------------------------
# POLICY-AS-CODE INVESTIGATION
# --------------------------------------------------

st.markdown("### From Legal Requirement to Inspectable Rule")


st.write(
    """
    The PoC investigates how a legal requirement can be decomposed into
    conditions that InspectR could evaluate using information represented
    in a pipeline blueprint.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Rule Path")

    st.code(
        """
AIA Provision
      ↓
Legal Conditions
      ↓
Machine-readable PaC Rule
      ↓
Applicability
Does this rule apply here?
      ↓
Required Evidence
What must the blueprint tell us?
      ↓
Evaluation
What does the available evidence establish?
      ↓
OK / FAIL / HUMAN
""",
        language="text",
    )

with col2:
    st.markdown("#### Proposed Evaluation Outcomes")

    st.success(
        "OK — sufficient blueprint evidence supports satisfaction "
        "of the encoded requirement."
    )

    st.error(
        "FAIL — sufficient blueprint evidence demonstrates "
        "non-conformance with the encoded requirement."
    )

    st.warning(
        "HUMAN — the available blueprint evidence is insufficient "
        "for an automated determination."
    )

    st.markdown("#### Key Question")

    st.write(
        """
        **Does the current inLUMEN blueprint provide the information
        InspectR needs to determine applicability and evaluate the rule?**
        """
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
<style>
.inspectr-footer {
    position: fixed;
    bottom: 20px;
    left: 270px;
    color: #8a8a8a;
    font-size: 0.85rem;
    z-index: 999;
}
</style>

<div class="inspectr-footer">
    InspectR PoC — Architecting a Compliance Engine for Multi-Agent Data Pipeline Ecosystems
</div>
""",
    unsafe_allow_html=True,
)
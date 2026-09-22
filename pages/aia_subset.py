import streamlit as st


st.subheader("EU AI Act Subset")

st.write(
    """
    The current InspectR PoC uses a small, provisional subset of the
    EU Artificial Intelligence Act (AIA) to demonstrate how legal
    requirements can be operationalized as machine-executable
    Policy-as-Code and evaluated against the TK pipeline blueprint.

    The purpose at this stage is to demonstrate the InspectR mechanism,
    not to establish full AI Act compliance. The final regulatory subset
    and its technical interpretation require further legal analysis and
    validation.
    """
)

st.divider()

# --------------------------------------------------
# CURRENT POC RULES
# --------------------------------------------------

st.markdown("### Current PoC Rules")

st.markdown(
    """
| InspectR Rule | AIA Provision | PoC Focus | Blueprint Evidence |
|---|---|---|---|
| `AIA-10` | [Article 10 — Data and data governance](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_10) | Data source provenance and approval | `source_id`, `approved_source` |
| `AIA-12` | [Article 12 — Record-keeping](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_12) | Logging capability | `has_logging` |
| `AIA-14` | [Article 14 — Human oversight](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689#art_14) | Human oversight for automated decision support | `automated_decision_support`, `human_oversight` |
"""
)

st.caption(
    "PoC operationalization: these checks represent selected aspects "
    "of the provisions for technical demonstration. They do not establish "
    "full conformity with Articles 10, 12, or 14."
)

st.caption(
    "Legal source: Regulation (EU) 2024/1689 — Artificial Intelligence Act, EUR-Lex."
)

st.divider()


# --------------------------------------------------
# POLICY-AS-CODE
# --------------------------------------------------

st.markdown("### From Legal Requirement to Inspectable Rule")

st.write(
    """
    InspectR translates selected regulatory requirements into explicit
    Rego rules. OPA evaluates these rules against evidence declared in
    the pipeline blueprint.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Evaluation Path")

    st.code(
        """
AIA Provision
      ↓
PoC Operationalization
      ↓
Rego Policy
      ↓
Blueprint Evidence
      ↓
OPA Evaluation
      ↓
OK / FAIL / HUMAN
""",
        language="text",
    )


with col2:
    st.markdown("#### Evaluation Outcomes")

    st.success(
        "OK — available blueprint evidence satisfies "
        "the encoded rule."
    )

    st.error(
        "FAIL — available blueprint evidence does not satisfy "
        "the encoded rule."
    )

    st.warning(
        "HUMAN — the available evidence is insufficient for "
        "an automated determination or requires human review."
    )


st.divider()

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
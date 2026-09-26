import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="PaC Compliance Challenges",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Header Section
st.title("🫧From fuzzy legislation to deterministic software logic")
st.markdown(
    "Implementing automated compliance checks via tools like Open Policy Agent (OPA) and Rego "
    "uncovers a fundamental challenge: **the semantic gap**. This problem arises from the multi-tier "
    "process of translating high-level, subjective legislation into binary, deterministic software logic."
    "To build a maintainable compliance validation system, engineering teams must not interpret "
    "legislation directly. Instead, organizations must decouple the process into three distinct layers: " \
    "**The Three-Tier PaC Translation Framework**."
)

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Tier 1: Regulation")
    st.markdown(
        "**Source:** Sovereign Governments\n\n"
        "**Nature:** Subjective, intentionally fuzzy, and flexible. "
        "Written to accommodate future advancements and contextual application.\n\n"
        "**Example:** GDPR Article 5 mandates *'appropriate technical and organizational measures'* "
        "to secure personal data."
    )

with col2:
    st.subheader("Tier 2: Policy")
    st.markdown(
        "**Source:** Corporate Governance & Legal\n\n"
        "**Nature:** Interpretative and contextual. Converts legal ambiguity into "
        "concrete organizational mandates and architecture baselines.\n\n"
        "**Example:** *'To satisfy GDPR Article 5, all data pipelines processing personally identifiable "
        "information (PII) must utilize AES-256 at-rest encryption.'*"
    )

with col3:
    st.subheader("Tier 3: Engineering PaC")
    st.markdown(
        "**Source:** Platform & Security DevOps\n\n"
        "**Nature:** Deterministic, literal, and binary. Assesses structured data configurations "
        "against static assertions to yield a strict pass or fail output.\n\n"
        "**Example:** A Rego policy validating that a JSON blueprint sets the flag "
        "`encryption_at_rest` to true."
    )

st.divider()

# Concrete Code Breakdown
st.header("Concrete Implementation Example")
st.markdown(
    "Below is a demonstration of how a data pipeline blueprint is automatically audited against "
    "the Tier 2 internal corporate interpretation of the EU AI Act."
)

code_col1, code_col2 = st.columns(2)

with code_col1:
    st.subheader("Data Pipeline Blueprint (input.json)")
    st.markdown("This metadata block describes the architectural traits of a newly deployed data pipeline.")
    json_example = """{
  "pipeline_name": "hr_resume_screening_ai",
  "ai_system": {
    "use_case": "employment_recruitment",
    "risk_classification": "high",
    "logging_enabled": false,
    "has_human_in_the_loop": true
  }
}"""
    st.code(json_example, language="json")
    # Core Friction Points
    st.header("Core Operational Friction Points")

    st.info(
        "1. **The Context Vacuum:** OPA cannot inspect business intent or evaluate subjective clauses like "
        "'legitimate interest'. It can only assert against declared structural attributes provided in the metadata input.\n"
        "2. **Garbage In, Garbage Out:** The enforcement model is entirely dependent on the integrity of the data blueprint. "
        "If engineers categorize data fields incorrectly or intentionally obfuscate high-risk variables, the tool will generate false compliance assurances.\n"
        "3. **Regulatory Evolution:** Court rulings, guidelines, and regulatory frameworks frequently change. "
        "This necessitates an explicit lifecycle update mechanism where legal mutations systematically trigger policy modifications at the code tier."
    )

with code_col2:
    st.subheader("Rego Compliance Policy (aiact.rego)")
    st.markdown("The OPA rules compile corporate policy into binary logic while embedding legal traceability.")
    rego_example = """package compliance.aiact

default allow = false

allow if count(deny) == 0

# Rule: High-Risk AI systems (Annex III) require automated logging (Art. 12)
deny[compliance_error] {
    input.ai_system.risk_classification == "high"
    input.ai_system.logging_enabled == false
    
    compliance_error := {
        "status": "FAIL",
        "rule_id": "SEC-AI-012",
        "message": "High-risk AI pipeline missing automated logging framework.",
        "traceability": {
            "internal_policy": "Corporate AI Governance Standard v2.1 (Section 4.2)",
            "regulation_reference": "EU AI Act - Article 12 (Logging)"
        }
    }
}"""
    st.code(rego_example, language="rego")

st.divider()

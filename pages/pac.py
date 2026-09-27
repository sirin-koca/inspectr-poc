import streamlit as st

st.title("Policy-as-Code")
st.write(
    "Policy-as-Code is the engineering practice of expressing an operational compliance "
    "interpretation as executable rules. InspectR keeps those rules separate from the Streamlit application."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Interpretation")
    st.markdown(
        "Requirement -> interpretation -> evidence model\n\n"
        "The rule author defines applicability and required blueprint evidence."
    )

with col2:
    st.subheader("OPA / Rego")
    st.markdown(
        "Blueprint + policy -> decision\n\n"
        "OPA independently evaluates the static blueprint against Rego conditions."
    )

with col3:
    st.subheader("InspectR")
    st.markdown(
        "Decision -> explanation\n\n"
        "Streamlit orchestrates the evaluation and presents status, evidence, reason, and remedy."
    )

st.divider()
st.header("Active TK/MUNDAT policy")
st.code(
    """TK/MUNDAT blueprint
        |
        | nodes, connections, compliance_extensions
        v
Python evaluator
        |
        +-- policy.rego
        |   TK-STRUCT-01
        |   TK-DATA-01
        |   TK-TRACE-01
        |   TK-RISK-01
        |   TK-HUMAN-01
        v
OPA: data.inspectr.results
        |
        v
OK / FAIL / HUMAN
        |
        v
Evidence + reason + rule reference + remedy""",
    language="text",
)

st.header("Why this separation matters")
st.markdown(
    """
    - Python does not contain the compliance decision conditions.
    - Rego is independently testable and can be changed without rewriting the UI.
    - The blueprint is the evidence input, not the policy.
    - OPA is the decision engine, not the legal interpreter.
    - InspectR reports what the encoded rule supports and exposes its limits.
    """
)

st.info(
    "The architecture is correct for this PoC when policy remains in Rego, the blueprint supplies evidence, "
    "and the application only orchestrates and explains the result."
)
import streamlit as st

st.subheader("Policy-as-Code - PaC Framework")
st.markdown(
    """
    PaC is a software engineering approach to compliance that represents regulatory requirements as machine-readable rules.
    PaC uses Open Policy Agent (OPA) and its query language, Rego, **decouples policy decision-making from application logic** 
    and infrastructure enforcement to automate compliance checks.
    """)

st.divider()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("#### 1. Policy-as-Code")
    st.markdown("""
    **What should be checked?**

    A compliance requirement is translated into an explicit rule.

    `Requirement → Rego rule`

    The policy remains separate from the application code.
    """)

with col2:
    st.markdown("#### 2. Open Policy Agent")
    st.markdown("""
    **Does the blueprint satisfy the rule?**

    OPA receives the pipeline blueprint and evaluates its declared
    properties against the Rego policies.

    `Blueprint + Policy → Evaluation`
    """)

with col3:
    st.markdown("#### 3. InspectR")
    st.markdown("""
    **What does the result mean?**

    InspectR orchestrates the evaluation and presents the finding.

    `OK · FAIL · HUMAN`

    Each finding can include **evidence, reason, legal reference,
    and remedy**.
    """)

st.divider()

st.markdown("### How it works in this project")

st.code(
"""TK pipeline blueprint (JSON)
        │
        │  declared evidence
        ▼
   InspectR
        │
        ├──── Rego policies
        │     AIA-10
        │     AIA-12
        │     AIA-14
        │
        ▼
       OPA
        │
        │  evaluates evidence against rules
        ▼
 OK / FAIL / HUMAN
        │
        ▼
Evidence · Reason · Legal reference · Remedy""",
    language="text",
)

st.info(
    "Core idea: the pipeline provides the evidence, Rego defines the "
    "rules, OPA evaluates them, and InspectR makes the findings visible."
)
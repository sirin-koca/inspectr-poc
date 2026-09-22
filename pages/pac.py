import streamlit as st

st.subheader("Policy-as-Code Framework")

st.markdown("""
### From regulation to executable inspection

InspectR uses **Policy-as-Code (PaC)** to represent selected compliance
requirements as rules that software can evaluate.

**Rego** is the policy language used to write these rules.  
**Open Policy Agent (OPA)** is the engine that executes them.
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
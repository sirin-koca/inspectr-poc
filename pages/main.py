import streamlit as st

st.title("InspectR")
st.caption("**Proof of concept** Compliance automation engine for data pipelines")

st.image("images/main.png", use_container_width=True)

st.divider()

# --------------------------------------------------
# OVERVIEW
#What is InspectR?
#Why is it needed?
#What is the TK case?
#How does the architecture work?
#What rules are active?
#Can it run?
#What is the research contribution?
# --------------------------------------------------

st.subheader("Compliance Engine Logic")

st.code(
    """Organisational Policy
        ↓
Required Design-Time Evidence
        ↓
Pipeline Blueprint
        +
Policy-as-Code (Rego)
        ↓
Open Policy Agent (OPA)
        ↓
OK / FAIL / HUMAN
        ↓
Evidence · Reason · Rule Reference · Remedy""",
    language="text",
)

st.caption(
    "Blueprint = evidence · Policy = conditions · "
    "Rego = executable policy · OPA = evaluator"
)

st.divider()

# --------------------------------------------------
# SEMANTIC GAP
# --------------------------------------------------

st.subheader("The Semantic Gap")

st.markdown(
    """
    **Compliance requirements are contextual. Software logic is deterministic.**

    Policy-as-Code bridges this gap by translating defined organisational
    policy conditions into executable rules that can be evaluated against
    explicit pipeline evidence.
    """
)

st.code(
    "Policy requirement → Evidence requirement → Rego rule → OPA evaluation",
    language="text",
)

st.divider()

# --------------------------------------------------
# POC BOUNDARY
# --------------------------------------------------

st.subheader("PoC Boundary")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        **This PoC**

        - TK/MUNDAT use case
        - Static inLUMEN JSON blueprint
        - Rego Policy-as-Code
        - OPA evaluation
        - Design-time inspection
        """
    )

with col2:
    st.markdown(
        """
        **Not claimed**

        - Legal compliance certification
        - Runtime verification
        - Automated legal interpretation
        - Intermediate Representation (IR)
        """
    )
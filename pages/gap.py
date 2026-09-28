import streamlit as st

st.title("The Semantic Gap")
st.caption("From compliance requirements to deterministic software logic")

st.markdown(
    """
    Legal and organisational requirements are expressed for **human interpretation**.
    Policy engines evaluate **explicit, deterministic conditions**.

    **The semantic gap is the translation between these two forms.**
    """
)

st.divider()

# --------------------------------------------------
# THE GAP
# --------------------------------------------------

left, middle, right = st.columns([1, 0.8, 1])

with left:
    st.subheader("Human-readable")
    st.markdown(
        """
        **Regulation / Policy**

        - Contextual
        - Semantic
        - May require judgement
        - May contain ambiguity
        """
    )

with middle:
    st.subheader("Semantic Gap")
    st.markdown(
        """
        What does the requirement **mean operationally?**

        What must be **observable?**

        What can software **actually evaluate?**
        """
    )

with right:
    st.subheader("Machine-evaluable")
    st.markdown(
        """
        **Policy-as-Code**

        - Explicit input
        - Defined conditions
        - Deterministic logic
        - Machine-checkable
        """
    )

st.divider()

# --------------------------------------------------
# TRANSLATION
# --------------------------------------------------

st.subheader("Operationalisation")

st.code(
    """Regulatory Requirement
        ↓
Organisational Policy
        ↓
Pipeline Requirement / Condition
        ↓
Required Observable Evidence
        ↓
Executable Rego Rule
        ↓
OPA Evaluation""",
    language="text",
)

st.markdown(
    """
    The critical step is **not converting legal text directly into code**.

    It is making the intermediate interpretation explicit:
    **what condition must hold, what evidence represents it, and what rule evaluates it.**
    """
)

st.divider()

# --------------------------------------------------
# INSPECTR
# --------------------------------------------------

st.subheader("Where InspectR Operates")

st.markdown(
    """
    InspectR starts from **defined organisational policy conditions** and evaluates
    their observable representation in a pipeline blueprint.

    **InspectR does not perform legal interpretation.**
    It operationalises explicit policy conditions as testable design-time controls.
    """
)

st.code(
    """Policy condition
      ↓
Evidence requirement
      ↓
Blueprint evidence ──→ Rego rule
                         ↓
                        OPA
                         ↓
                  OK / FAIL / HUMAN""",
    language="text",
)

st.divider()

# --------------------------------------------------
# AUTOMATION BOUNDARY
# --------------------------------------------------

st.subheader("Automation Boundary")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        **Software can evaluate**

        Explicit evidence against explicit conditions.
        """
    )

with col2:
    st.markdown(
        """
        **Software cannot establish**

        The legal meaning, completeness, or correctness
        of the policy interpretation itself.
        """
    )

st.info(
    "A deterministic result is only as valid as the policy interpretation, "
    "evidence model, and input evidence on which it depends."
)
import streamlit as st

st.title("InspectR")
st.caption("Policy-as-Code for design-time pipeline inspection")

st.markdown(
    """
    InspectR is a proof-of-concept architecture for translating selected
    regulatory and governance requirements into explainable, machine-checkable
    policy findings over a static data-pipeline blueprint.
    """
)

st.image("images/main.png", width=1000)
st.divider()

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("What this PoC demonstrates")
    st.markdown(
        """
        - A pipeline blueprint provides design-time evidence.
        - Policy is kept outside the Python application.
        - OPA evaluates Rego independently of the UI.
        - InspectR explains each result with evidence, reason, and remedy.
        """
    )

with col2:
    st.subheader("What InspectR does not claim")
    st.markdown(
        """
        InspectR does not certify compliance, encode the law directly, or
        replace legal interpretation. It evaluates whether declared evidence
        satisfies an explicitly defined organizational policy.
        """
    )

st.divider()

st.subheader("The semantic gap")
st.markdown(
    """
    Regulation is broad, contextual, and open to interpretation. Rego is
    deterministic and can evaluate only explicit data. The central research
    problem is therefore the translation between them:
    """
)
st.code(
    "Regulatory requirement\n"
    "        ↓\n"
    "Organizational interpretation\n"
    "        ↓\n"
    "Required blueprint evidence\n"
    "        ↓\n"
    "Policy-as-Code in Rego\n"
    "        ↓\n"
    "OK / FAIL / HUMAN",
    language="text",
)

st.subheader("The generalization challenge")
st.markdown(
    """
    InspectR must remain a generic engine. Organizations should be able to
    provide their own policy definitions without hard-coding every policy into
    InspectR itself. This PoC uses the TK/MUNDAT policy as a concrete test case
    to demonstrate the architecture; a reusable policy-pack or policy-profile
    mechanism belongs to the future InspectR architecture.
    """
)

st.info(
    "Current boundary: the TK/MUNDAT blueprint is evaluated directly by OPA/Rego. "
    "No Intermediate Representation is implemented in this PoC."
)


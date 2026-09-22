import streamlit as st

# --------------------------------------------------
# MAIN
# --------------------------------------------------

st.title("InspectR - policy engine") 
st.code("Proof of Concept - TK Use Case")
st.image(
    "images/main.png",
    width=1000,
)
st.divider()

# --------------------------------------------------
# POC OVERVIEW
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Compliance Rules")
    st.write(
        """
        Selected **EU AI Act (AIA) requirements** investigated as
        machine-readable Policy-as-Code.
        """
    )

with col2:
    st.markdown("#### InspectR")
    st.write(
        """
        Inspect the **TK inLUMEN pipeline blueprint**
        using design-time evidence.
        """
    )

with col3:
    st.markdown("#### Evaluation")
    st.write(
        """
        Determine what can be concluded and where
        **evidence is insufficient**.
        """
    )


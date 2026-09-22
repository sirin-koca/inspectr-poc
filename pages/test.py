import streamlit as st
st.subheader("subheader")

st.divider()

st.markdown('Rego is **_really_ cool**.')
st.metric("Accuracy", "90%", "+2.5")


# --------------------------------------------------
# TESTS
# --------------------------------------------------

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
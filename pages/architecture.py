import streamlit as st

st.subheader("InspectR Architecture")

st.warning(
    "The PoC scope evaluates the JSON pipeline blueprint directly. "
    "No Intermediate Representation (IR) is implemented."
)

st.image(
    "images/arch-2.png",
    caption="InspectR Architecture",
    width=1100,
)

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

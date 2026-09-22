import streamlit as st

st.subheader("InspectR PoC Architecture")

st.write(
    """
    The architecture evaluates a pipeline blueprint
    against a machine-readable Policy-as-Code ruleset derived from the
    selected EU AI Act provisions.
    """
)

st.caption(
    "PoC scope: the JSON pipeline blueprint is evaluated directly. "
    "No Intermediate Representation (IR) is implemented."
)

st.divider()

st.image(
    "images/arch.jpg",
    caption="InspectR PoC Architecture",
    width=400,
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

import streamlit as st

st.header("PoC Flow")
st.write("__TK blueprint → taxonomy/rules → InspectR engine → OK/FAIL/HUMAN + evidence + remedy.__")
st.divider()
st.image(
    "images/poc.jpg",
     width=500,
)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Input")
    st.write(
        "A structured TK pipeline blueprint containing pipeline stages "
        "and available metadata."
    )

with col2:
    st.subheader("2. Inspect")
    st.write(
        "InspectR evaluates observable pipeline properties against "
        "machine-readable compliance constraints."
    )

with col3:
    st.subheader("3. Output")
    st.write(
        "InspectR returns OK, FAIL, or HUMAN together with evidence, "
        "reasoning, and remediation suggestions."
    )

st.divider()

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

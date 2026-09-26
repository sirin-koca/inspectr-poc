import streamlit as st

st.set_page_config(
    page_title="InspectR | Test Page🎈",
    page_icon="🔎",
    layout="wide"
)

st.subheader("TEST")

st.subheader("Compliance Architecture Layers")

# Layer 1 Card
with st.container(border=True):
    st.markdown("#### Layer 1 — Regulation (source of truth)")
    st.markdown("GDPR / AIA articles, recitals, obligations.")

st.markdown("⬇️")

# Layer 2 Card
with st.container(border=True):
    st.markdown("#### Layer 2 — Governance model (local policy / interpretation)")
    st.markdown("**Organization's compliance framework:**")
    st.markdown(
        "- What counts as \"high-risk\"\n- What metadata must be present\n- What documentation is required\n- What oversight mechanisms are acceptable"
    )
    st.caption("_This is where legal ➔ technical mapping happens._")

st.markdown("⬇️")

# Layer 3 Card
with st.container(border=True):
    st.markdown("#### Layer 3 — Policy-as-Code (OPA/Rego)")
    st.markdown("Executable rules derived from the governance model:")
    st.code("deny[msg] { missing_metadata }")
    st.code('require_human_review { ai_component.risk == "high" }')
    st.code("allow { pipeline.step.purpose in approved_purposes }")

import streamlit as st

st.subheader("About InspectR")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Status", value="Active", delta="Normal")
col2.metric(label="Errors", value="0", delta=None)
col3.metric(label="Mode", value="Code Execution")
col4.metric(label="Queue", value="Empty")

st.divider()

tab1, tab2, tab3 = st.tabs(["📊 Overview", "⚙️ Configuration", "❌ Error Logs"])

with tab1:
    st.info("General high-level overview text.")

with tab2:
    st.code("# Config settings\nTIMEOUT = 30", language="python")

with tab3:
    st.error("System traceback history.")

st.divider()


st.subheader("Compliance Architecture Layers")

# Layer 1 Card
with st.container(border=True):
    st.markdown("#### Layer 1 — Regulation (source of truth)")
    st.markdown("GDPR / AIA articles, recitals, obligations.")

st.markdown("⬇️")

# Layer 2 Card
with st.container(border=True):
    st.markdown("#### Layer 2 — Governance model (local policy / interpretation)")
    st.markdown(
        "What oversight mechanisms are acceptable"
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

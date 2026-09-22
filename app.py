import streamlit as st

# --------------------------------------------------
# APP CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="InspectR PoC",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "blueprint" not in st.session_state:
    st.session_state["blueprint"] = None

if "blueprint_filename" not in st.session_state:
    st.session_state["blueprint_filename"] = None

if "evaluation_results" not in st.session_state:
    st.session_state["evaluation_results"] = None

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

pages = [
    st.Page("pages/main.py", title="Main", default=True),
    st.Page("pages/research.py", title="Research"),
    st.Page("pages/tk_uc.py", title="TK UC"),
    st.Page("pages/taxonomy.py", title="Taxonomy"),
    st.Page("pages/aia_subset.py", title="AIA Subset"),
    st.Page("pages/pac.py", title="PaC"),
    st.Page("pages/architecture.py", title="Architecture"),
    st.Page("pages/evaluation.py", title="Evaluation"),
]

pg = st.navigation(pages)

# --------------------------------------------------
# GLOBAL FOOTER
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

# --------------------------------------------------
# RUN SELECTED PAGE
# --------------------------------------------------

pg.run()
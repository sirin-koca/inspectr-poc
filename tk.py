import streamlit as st

st.set_page_config(page_title="TK Use Case | InspectR", layout="wide")

st.title("TK Use Case — Trondheim Kommune")
st.caption("MUNDAT: Compliant, data-driven city of Trondheim")

# -------------------------------------------------------------------
# 1. PURPOSE
# -------------------------------------------------------------------

st.subheader("1. Use Case")

st.info(
    """
    **Goal:** Enable more efficient and compliant municipal data sharing.

    TK's process covers the lifecycle from receiving a data request to
    identifying, extracting, integrating, assessing, and securely sharing data.
    """
)

st.markdown(
    """
    **Data request and sharing workflow**

    `Data Request` → `DPIA / Risk Assessment` → `Identify Data Sources`
    → `Extract Data` → `Integrate Dataset` → `Final Risk Assessment`
    → `Secure Sharing`
    """
)

# -------------------------------------------------------------------
# 2. CORE COMPLIANCE CHALLENGES
# -------------------------------------------------------------------

st.subheader("TK Compliance Challenges")

challenges = [
    {
        "Challenge": "No systematic request process",
        "Problem": "No consistent overview of how data-sharing requests are handled and by whom.",
    },
    {
        "Challenge": "Unclear compliance applicability",
        "Problem": "Uncertainty about which data sources require compliance processes.",
    },
    {
        "Challenge": "Insufficient compliance metadata",
        "Problem": "Missing data dictionaries, metadata, and compliance annotations.",
    },
    {
        "Challenge": "PII / sensitive-data identification",
        "Problem": "Combining multiple sources makes re-identifiable PII and sensitive data difficult to identify.",
    },
    {
        "Challenge": "Complex compliance assessment",
        "Problem": "Compliance and risk must be assessed across extraction, integration, and sharing.",
    },
    {
        "Challenge": "Insufficient documentation",
        "Problem": "Better documentation of datasets, processing, and compliance measures is required.",
    },
]

st.dataframe(
    challenges,
    use_container_width=True,
    hide_index=True,
)

st.warning(
    """
    **Core problem**

    TK needs to share municipal data efficiently and compliantly,
    but lacks sufficiently systematic processes, compliance information,
    metadata, and automation to support consistent compliance assessment.
    """
)

# -------------------------------------------------------------------
# 3. BASELINE LIMITATION
# -------------------------------------------------------------------

st.subheader("3. InspectR Baseline")

left, right = st.columns(2)

with left:
    st.markdown(
        """
        #### What TK provides
        - High-level data-sharing workflow
        - Compliance challenges
        - User stories
        - Functional requirements
        - Example datasets
        """
    )

with right:
    st.markdown(
        """
        #### What is not sufficiently specified
        - Concrete technical pipeline
        - Detailed data classifications
        - Compliance metadata
        - Applicable obligations per processing condition
        - Explicit technical safeguards per scenario
        """
    )

st.info(
    """
    **Baseline decision:**  
    First represent only what the TK document actually specifies and evaluate
    what InspectR can determine from that evidence.
    """
)

# -------------------------------------------------------------------
# 4. POC STRATEGY
# -------------------------------------------------------------------

st.subheader("4. PoC Strategy")

st.markdown(
    """
    ### TK Baseline → Compliance Extension → InspectR Evaluation

    **① TK Baseline**  
    Minimal pipeline derived from the documented TK workflow.

    ↓

    **② Baseline Test**  
    Evaluate what can be determined from the available pipeline evidence.

    ↓

    **③ Synthetic Compliance Extension**  
    Add explicit compliance-relevant evidence and controls for controlled testing.

    ↓

    **④ InspectR Evaluation**  
    Evaluate Policy-as-Code rules and produce **OK / FAIL / HUMAN** decisions.
    """
)

st.success(
    """
    **Purpose of the extension**

    The Compliance Extension is an experimental artefact used to demonstrate
    and evaluate InspectR's capabilities. It is **not presented as TK's actual
    pipeline or compliance implementation**.
    """
)
import streamlit as st
# --------------------------------------------------
# 1. APP CONFIGURATION 
# -------------------------------------------------

# --------------------------------------------------
# 2. THE ONE GLOBAL CSS BLOCK TO RULE THEM ALL
#    (Put all your app-wide tweaks right here!)
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* A. Makes the navigation menu text bigger */
    [data-testid="stSidebarNavItems"] span {
        font-size: 1.15rem !important; 
    }
    [data-testid="stSidebarNavItems"] svg {
        transform: scale(1.1); 
    }

    /* B. Destroys the annoying default top space/padding on every page */
    section.stMain .block-container {
        padding-top: 1rem !important; 
        padding-bottom: 1rem !important;
    }

    /* C. Custom reusable class for your markdown background fields */
    .custom-card {
        background-color: #f0f2f6; 
        padding: 15px; 
        border-radius: 8px; 
        color: #31333F;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("InspectR Architecture")

st.warning(
    "This PoC deliberately evaluates the inLUMEN JSON blueprint directly. "
    "No Intermediate Representation (IR) is implemented for KISS purposes."
)

st.image(
    "images/arch-inspectr.jpeg",
    caption="InspectR",
)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
    """
    ### Why this architecture?

    1. **Blueprint** - the pipeline topology: the TK/MUNDAT pipeline and declared evidence.
    2. **Policy** - the operational interpretation encoded in Rego.
    3. **Decision engine** - InspectR utilizing OPA evaluates the policy independently from the application logic.
    4. **Evaluation** - InspectR reports the decision and evidence to the user - optionally triggers the agentic work-flow for self-correction.

    - Decoupling Blueprint from Logic: Heterogeneous data pipeline artifacts are parsed into a Unified Graph Intermediate Representation (IR). 
    Rego policies evaluate the Graph IR, not raw code. This makes IncspectR vendor-agnostic and scalable. 
    - Shift-Left Compliance: Catching non-compliance at design-time (CI/CD / pull request phase) prevents 
    costly runtime compliance failures and data contamination. 
    - Tri-State Output (OK / FAIL / HUMAN): Standard linters offer binary true/false decisions. 
    Real-world compliance requires handling ambiguity by routing complex legal edge cases to human compliance 
    officers (HUMAN). 
    """
)

with col2:
    st.code(
            """
            LAW
                1. GDPR provision: Use Case TK 
                2. AIA: Use Case X 
            ↓
            Policy (Organisational requirements)
            ↓
            Observable evidence in the blueprint
            ↓
            Executable PaC rule
            ↓
            Evaluation: InspectR Engine
            ↓
            OK/FAIL/HUMAN
            """,
            language="text",                    
)  
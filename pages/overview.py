import streamlit as st

st.set_page_config(
    page_title="InspectR | Overview",
    page_icon="🔎",
    layout="wide",
)

st.title("InspectR PoC")
st.code("TK/MUNDAT case - direct static blueprint evaluation")

st.info(
    "InspectR is a proof-of-concept architecture for design-time compliance tooling. "
    "It investigates how selected regulatory and governance requirements can be operationalized "
    "as explainable Policy-as-Code checks over static data-pipeline blueprints. "
    "This PoC does not determine legal compliance as a whole."
)

st.header("The semantic gap")
st.write(
    "Regulations and business requirements are contextual and principle-based. "
    "OPA and Rego require explicit fields and deterministic conditions. InspectR studies the "
    "translation between those two forms without hiding the interpretation."
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.subheader("1. Requirement source")
    st.markdown(
        "Regulations, guidance, and TK/MUNDAT requirements provide the source material. "
        "They are not directly executable."
    )

with col2:
    st.subheader("2. Operational interpretation")
    st.markdown(
        "A researcher or organization defines what the requirement means in this context, "
        "what evidence is required, and what counts as sufficient or ambiguous evidence."
    )

with col3:
    st.subheader("3. Policy-as-Code")
    st.markdown(
        "The interpretation becomes an independent Rego policy. OPA evaluates that policy "
        "against the evidence declared in the blueprint."
    )

st.divider()
st.header("Traceability model")
st.code(
    """Requirement or use-case need
        |
        v
Operational interpretation
        |
        v
Required evidence
        |
        v
TK/MUNDAT blueprint fields
        |
        v
Rego condition evaluated by OPA
        |
        v
OK / FAIL / HUMAN
        |
        v
Evidence + reason + rule reference + remedy""",
    language="text",
)

st.warning(
    "GDPR and the EU AI Act are possible regulatory sources for the broader InspectR project. "
    "The active rules in this TK PoC are local design-time checks, not a complete implementation of either law."
)

st.header("PoC boundary")
st.markdown(
    """
    - The blueprint is evaluated directly.
    - No Intermediate Representation is implemented in this PoC.
    - The pipeline is not executed.
    - Results are correct relative to the encoded operational rule, not proof of legal compliance.
    - Missing or ambiguous evidence is separated from explicit negative evidence.
    """
)
import streamlit as st

st.set_page_config(
    page_title="InspectR | Overview",
    page_icon="🔎",
    layout="wide"
)

st.code("Proof of Concept - TK Use Case")
st.info(
    """
    **InspectR** is a design-time compliance inspection engine for data/AI pipeline specifications.
    It evaluates explicitly defined, machine-checkable compliance conditions against evidence available in a pipeline blueprint using Policy-as-Code (OPA/Rego).
    **Boundary**: InspectR evaluates encoded technical conditions; it does not determine legal compliance as a whole.
    """
) 
# -------------------------------------------------------------------
# Core concepts
# -------------------------------------------------------------------
st.header("Compliance, Policy, Regulation?")

col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.subheader("Terminology")
    # Terms such as **compliance**, **policy**, and **Policy-as-Code**
    # can mean different things across regulatory, governance,
    # security, and engineering contexts.
    with col1:
        st.markdown("""
        For InspectR:

        - **Regulations** = external, legally binding requirements and obligations (eg. GDPR, AIA).  
        - **Policies** = internal, organization‑defined rules expressing how you comply with those regulations.  
        - **Policy-as-Code (PaC)** is the paradigm, like IaC (Infrastructure-as-Code).
        - **OPA (Open Policy Agent)** is the policy evaluation engine.
        - **Rego** is the policy language.
        - **GDPR / EU AI Act** requirements are not inherently encoded in OPA or Rego.
        - Regulatory requirements must first be operationalised into explicit, machine-checkable rules.
        """)
        st.markdown("""
            A **regulation** is a *law* created by the EU legislature. It is:
            - **Externally imposed**
            - **Legally binding**
            - **Non-negotiable**
            - **Technology-agnostic**
            - **High-level and principle-based**
        
            Examples:
            - GDPR Art. 5: *Data minimization*
            - GDPR Art. 25: *Privacy by design*
            - AIA Art. 9: *Risk management system*
            - AIA Art. 10: *Data governance and quality*
            - AIA Art. 14: *Human oversight*
        
            These are **not executable**. They are **legal obligations**, not machine-readable rules.
            """)
       
    with col2:
        st.subheader("Compliance Layers")
        st.markdown("""
        Regulatory requirements must first be translated into
        explicit, machine-checkable rules. Than, InspectR can evaluate whether the evidence 
        is present in a pipeline specification and if the evidence satisfies those defined rules.
        """)                
       # Layer 1 Card
        with st.container(border=True):
            st.markdown("#### Layer 1 — Regulation ")
            st.markdown("(source of truth)")    
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


    with col3:
        st.subheader("Traceability")

        st.code(
        """
        Legal requirement
                ↓
        Operational interpretation
                ↓
        Required evidence
                ↓
        Pipeline blueprint field(s)
                ↓
        Rego condition
                ↓
        OK / FAIL / HUMAN
                ↓
        Reason + Remedy""",
            language=None,
        )
        st.warning("""
        **Evidence principle**

        Absence of evidence is not automatically evidence of
        non-compliance.

        Insufficient or ambiguous evidence → **HUMAN**
        """)

        st.info("""
        **Interpretation boundary**

        InspectR checks defined technical compliance conditions against available design-time evidence and gives logical outputs: OK/FAIL/HUMAN.
        """)

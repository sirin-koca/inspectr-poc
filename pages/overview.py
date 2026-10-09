import streamlit as st

# Section 1: The Problem & Architectural Core
st.subheader("✰ Core Problem & Architecture")

col1, col2 = st.columns(2)
with col1:
    st.markdown("##### TK Compliance Bottleneck")
    st.error("""
    * **Post-Hoc & Manual:** Legal compliance checks occur manually after pipeline development or data collection.
    * **Semantic Gap:** Legal frameworks are qualitative; engineering specs are technical and execution-driven.
    * **Scale Barrier:** High resource burden on DPOs and compliance teams for routine data requests.
    """)
with col2:
    st.markdown("##### InspectR Approach")
    st.success("""
    * **Design-Time Static Verification:** Evaluating data pipeline configurations before deployment or execution to save time and cost.
    * **Policy-as-Code Engine:** Efficient PaC implementation of OPA/Rego evaluating structured pipeline blueprints against formalized policy logic.
    * **Tri-State Output:** Classifying pipeline states into deterministic results (`OK`/`FAIL`/`HUMAN`).
    """)

# Section 2: Key Research & Technical Contributions
st.subheader("✰ Key Technical Contribution")

with st.container():
    st.markdown("##### IR Layer: Unified Graph Metamodel (Intermediate Representation)")
    st.markdown("""
    * **Problem:** Data pipelines rely on fragmented, vendor-specific formats (Airflow DAGs, SQL, Terraform, custom JSON).
    * **Contribution:** A vendor-agnostic graph metamodel grounded in eg. W3C PROV-O data lineage and Data Privacy Vocabulary (DPV) standards.
    * **Research Novelty:** Decouples static compliance verification logic from execution engine runtimes, enabling a single policy set to evaluate heterogeneous pipeline specifications.
    """)

# Section 3: Grounding Use Case
st.subheader("✰ Grounding & Validation")
st.info("""
**Validation Scenario:** 
Evaluated against Trondheim Kommune's MUNDAT data-sharing workflow. 
InspectR automatically inspects extraction, integration, and anonymization 
pipelines to enforce data minimisation and consent rules prior to dataset 
delivery.
""")
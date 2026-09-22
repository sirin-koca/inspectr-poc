import json
import streamlit as st
from src.evaluator import evaluate  

st.caption(
    "Direct evaluation of the uploaded JSON pipeline blueprint "
    "against the InspectR Policy-as-Code ruleset. No Intermediate "
    "Representation (IR) is used in this PoC."
)

st.divider()


# =========================================================
# HORIZONTAL INSPECTR FLOW
# =========================================================

upload_col, arrow_1, evaluate_col, arrow_2, result_col = st.columns(
    [3.2, 0.35, 2.2, 0.35, 1.7],
    vertical_alignment="top"
)


# ---------------------------------------------------------
# UPLOAD
# ---------------------------------------------------------

with upload_col:
    st.markdown("### UPLOAD")

    uploaded_file = st.file_uploader(
        "JSON blueprint",
        type=["json"],
        label_visibility="visible",
    )

    if uploaded_file is not None:
        try:
            blueprint = json.load(uploaded_file)

            st.session_state["blueprint"] = blueprint
            st.session_state["blueprint_filename"] = uploaded_file.name

            # A new blueprint invalidates previous results
            st.session_state["evaluation_results"] = None

        except json.JSONDecodeError:
            st.error("Invalid JSON file.")

    if st.session_state.get("blueprint") is not None:
        st.success(
            f"Loaded: {st.session_state['blueprint_filename']}"
        )

        with st.expander("View blueprint"):
            st.json(st.session_state["blueprint"])


# ---------------------------------------------------------
# ARROW
# ---------------------------------------------------------

with arrow_1:
    st.markdown("<br><br><h3>→</h3>", unsafe_allow_html=True)


# ---------------------------------------------------------
# EVALUATE
# ---------------------------------------------------------

with evaluate_col:
    st.markdown("### EVALUATE")

    blueprint_available = st.session_state.get("blueprint") is not None

    evaluate_clicked = st.button(
        "Run InspectR",
        type="primary",
        use_container_width=True,
        disabled=not blueprint_available,
    )

    st.markdown(
        """
        **Evaluation output**

        - Evidence
        - Reason
        - Remedy
        - AIA provision
        """
    )

    if evaluate_clicked:
        blueprint = st.session_state["blueprint"]

        # InspectR engine will be connected here:
            
    if evaluate_clicked:

        with st.spinner("InspectR is evaluating the pipeline blueprint..."):

            results = evaluate(
                st.session_state["blueprint"]
            )

            st.session_state["evaluation_results"] = results

            st.success("Evaluation complete.")


# ---------------------------------------------------------
# ARROW
# ---------------------------------------------------------

with arrow_2:
    st.markdown("<br><br><h3>→</h3>", unsafe_allow_html=True)


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------
with result_col:
    st.markdown("### RESULT")

    results = st.session_state.get("evaluation_results")

    if results is None:
        st.caption("Run InspectR to generate results.")

    else:

        for result in results:

            status = result["status"]

            if status == "OK":
                st.success(f"OK — {result['rule']}")

            elif status == "FAIL":
                st.error(f"FAIL — {result['rule']}")

            else:
                st.warning(f"HUMAN — {result['rule']}")

            with st.expander(result["legal_reference"]):

                st.write("**Reason**")
                st.write(result["reason"])

                st.write("**Evidence**")
                st.json(result["evidence"])

                if result["remedy"]:
                    st.write("**Remedy**")
                    st.write(result["remedy"])

# ---------------------------------------------------------


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


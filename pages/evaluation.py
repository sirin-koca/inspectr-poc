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
    vertical_alignment="top",
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

            # Only reset results when a different file is uploaded
            if (
                st.session_state.get("blueprint_filename")
                != uploaded_file.name
            ):
                st.session_state["evaluation_results"] = None

            st.session_state["blueprint"] = blueprint
            st.session_state["blueprint_filename"] = uploaded_file.name

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
    st.markdown(
        "<br><br><h3>→</h3>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# EVALUATE
# ---------------------------------------------------------

with evaluate_col:
    st.markdown("### EVALUATE")

    blueprint_available = (
        st.session_state.get("blueprint") is not None
    )

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
        with st.spinner(
            "InspectR is evaluating the pipeline blueprint..."
        ):
            try:
                results = evaluate(
                    st.session_state["blueprint"]
                )

                st.session_state["evaluation_results"] = results

                st.success("Evaluation complete.")

            except Exception as error:
                st.session_state["evaluation_results"] = None
                st.error(f"Evaluation failed: {error}")


# ---------------------------------------------------------
# ARROW
# ---------------------------------------------------------

with arrow_2:
    st.markdown(
        "<br><br><h3>→</h3>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------

with result_col:
    st.markdown("### RESULT")

    results = st.session_state.get("evaluation_results")

    if results is None:
        st.caption("Run InspectR to generate results.")

    elif len(results) == 0:
        st.warning("No policy evaluation results returned.")

    else:
        for result in results:
            status = result.get("status", "HUMAN")
            rule = result.get("rule", "Unknown rule")

            if status == "OK":
                st.success(f"OK — {rule}")

            elif status == "FAIL":
                st.error(f"FAIL — {rule}")

            else:
                st.warning(f"HUMAN — {rule}")

            legal_reference = result.get(
                "legal_reference",
                "Policy details",
            )

            with st.expander(legal_reference):

                st.write("**Reason**")
                st.write(
                    result.get(
                        "reason",
                        "No reason provided.",
                    )
                )

                st.write("**Evidence**")
                st.json(
                    result.get(
                        "evidence",
                        {},
                    )
                )

                remedy = result.get("remedy")

                if remedy:
                    st.write("**Remedy**")
                    st.write(remedy)


# ---------------------------------------------------------
# FOOTER
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
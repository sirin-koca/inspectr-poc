import streamlit as st
# --------------------------------------------------
# TK COMPLIANCE FLOW
# --------------------------------------------------
st.markdown("### TK Compliance Flow")
st.write(
    """
    The Trondheim Kommune (TK) Use Case provides the application
        scenario used to demonstrate the InspectR PoC.
    The compliance flow defines the compliance-oriented process
    that forms the basis for the pipeline blueprint used in this PoC.
    """
)
st.image(
    "images/tk-uc-pl.jpg",
    caption="Trondheim Kommune Compliance Flow",
    width=900,
)
st.divider()
# --------------------------------------------------
# INLUMEN PIPELINE BLUEPRINT
# --------------------------------------------------

st.markdown("### inLUMEN Pipeline Blueprint")

st.write(
    """
    Based on the TK compliance flow, the pipeline blueprint below
    was created in inLUMEN. This blueprint represents the pipeline
    artifact subsequently provided to InspectR for compliance evaluation.
    """
)

st.image(
    "images/tk-uc-plbp.jpg",
    caption="TK Pipeline Blueprint created in inLUMEN",
    use_container_width=True,
)
    

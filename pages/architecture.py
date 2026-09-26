import streamlit as st

st.subheader("InspectR Architecture")

st.warning(
    "The PoC scope evaluates the JSON pipeline blueprint directly. "
    "No Intermediate Representation (IR) is implemented."
)

st.image(
    "images/arch-2.png",
    caption="InspectR Architecture",
    width=1100,
)

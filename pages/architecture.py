import streamlit as st

st.title("InspectR Architecture")

st.warning(
    "This PoC deliberately evaluates the inLUMEN JSON blueprint directly. "
    "No Intermediate Representation (IR) is implemented, to keep the architecture small and testable."
)

st.markdown(
    """
    ### Four separated concerns

    1. **Blueprint** - the TK/MUNDAT pipeline and declared evidence.
    2. **Policy** - the operational interpretation encoded in Rego.
    3. **Decision engine** - OPA evaluates the policy independently.
    4. **Application** - Streamlit orchestrates input and explains results.
    """
)

st.code(
    """TK/MUNDAT JSON blueprint
        |
        | nodes, connections, compliance_extensions
        v
Python evaluator
        |
        +-- policy.rego
        v
OPA query: data.inspectr.results
        |
        v
OK / FAIL / HUMAN + evidence + reason + remedy""",
    language="text",
)

st.image(
    "images/arch.png",
    caption="InspectR PoC architecture: direct blueprint evaluation without IR",
    width=1100,
)

st.info(
    "The future InspectR architecture may introduce an Intermediate Representation. "
    "That is intentionally outside this PoC boundary."
)
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

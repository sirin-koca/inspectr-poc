import plotly.express as px
import streamlit as st

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="InspectR Taxonomy Explorer", layout="wide")

st.popover(
    "About this taxonomy",
).write(
    """
    Machine-readable compliance taxonomy used by the InspectR PoC - TK Use Case.

    The InspectR taxonomy provides a structured overview of compliance concepts relevant to the PoC.
    It organizes the current problem space across the TK use case, pipeline structure, and selected 
    EU AI Act concepts. 
    
    The taxonomy supports analysis and rule development, and it is not evaluated directly by the InspectR engine.
    """
)
# -------------------------
# TAXONOMY SUMMARY TABLE
# -------------------------
overview_df = pd.DataFrame([
    {
        "Level": "Domain",
        "Meaning": "High-level compliance concern/category",
        "Example": "Data Governance",
    },
    {
        "Level": "Dimension",
        "Meaning": "Specific aspect within a domain",
        "Example": "Data Categories",
    },
    {
        "Level": "Atomic Element",
        "Meaning": "Concrete concept that can be evaluated",
        "Example": "Personal Data",
    },
    {
        "Level": "Constraint",
        "Meaning": "Machine-checkable requirement attached to the element",
        "Example": "Data Minimisation",
    },
    {
        "Level": "Rule Metadata",
        "Meaning": "Information used to execute and explain the constraint",
        "Example": "Logic, severity, message, regulatory reference",
    },
])

st.dataframe(
    overview_df,
    use_container_width=True,
    hide_index=True,
)

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# LOAD TAXONOMY
# --------------------------------------------------

TAXONOMY_PATH = Path("data/inspectr_taxonomy.json")

with open(TAXONOMY_PATH, "r", encoding="utf-8") as file:
    taxonomy = json.load(file)


# --------------------------------------------------
# CONVERT JSON TREE TO PLOTLY DATA
# --------------------------------------------------

labels = []
parents = []
levels = []
descriptions = []
colors = []
articles = []
links = []


def flatten_taxonomy(node, parent="", inherited_color="dodgerblue"):

    current_color = node.get("color", inherited_color)

    labels.append(node["label"])
    parents.append(parent)
    levels.append(node.get("level", ""))
    descriptions.append(node.get("description", ""))
    colors.append(current_color)
    articles.append(node.get("ai_act_article", ""))
    links.append(node.get("ai_act_link", ""))

    for child in node.get("children", []):
        flatten_taxonomy(
            child,
            parent=node["label"],
            inherited_color=current_color,
        )


flatten_taxonomy(taxonomy)


# --------------------------------------------------
# BUILD ICICLE
# --------------------------------------------------

fig = px.icicle(
    names=labels,
    parents=parents,
    values=[1] * len(labels),
    custom_data=[
        levels,
        descriptions,
        articles,
        links,
    ],
    title="InspectR PoC Taxonomy",
)


fig.update_traces(
    marker=dict(colors=colors),
    hovertemplate=(
        "<b>%{label}</b><br><br>"
        "<b>Level:</b> %{customdata[0]}<br>"
        "<b>Description:</b> %{customdata[1]}<br>"
        "<b>AIA provision:</b> %{customdata[2]}"
        "<extra></extra>"
    ),
    textinfo="label",
)


fig.update_layout(
    margin=dict(t=50, l=0, r=0, b=0),
    font=dict(size=16),
    title_font=dict(size=26),
)


st.plotly_chart(
    fig,
    use_container_width=True,
)
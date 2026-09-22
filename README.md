# InspectR

**Design-time compliance inspection for data pipeline ecosystems**

InspectR is a research prototype for investigating how regulatory requirements can be operationalized as **Policy-as-Code (PaC)** and evaluated against data pipeline blueprints before deployment.

The current proof of concept uses the **Trondheim Kommune (TK) use case** and selected provisions of the **EU AI Act** to demonstrate the approach.

## Core Architecture

```text
Pipeline Blueprint (JSON)
          │
          ▼
       InspectR
          │
          ▼
 Policy-as-Code (Rego)
          │
          ▼
 Open Policy Agent (OPA)
          │
          ▼
   Compliance Findings
   OK / FAIL / HUMAN
```

**System evidence ↔ Executable policy ↔ Independent decision engine**

The pipeline blueprint provides evidence. Rego defines the encoded compliance rules. OPA evaluates the evidence against those rules. InspectR presents the resulting findings.

## Current PoC

The current implementation demonstrates:

- design-time inspection of an inLUMEN/TK pipeline blueprint
- compliance rules externalized as Rego policies
- policy evaluation using Open Policy Agent
- structured `OK`, `FAIL`, and `HUMAN` outcomes
- evidence, reasoning, legal references, and remediation guidance

The current AI Act subset is **provisional** and used to demonstrate the technical mechanism. It does not establish legal compliance.

## Repository Structure

```text
inspectr-poc/
├── app.py          # Streamlit application
├── data/           # Pipeline blueprints and supporting data
├── pages/          # InspectR interface
├── policies/       # Rego Policy-as-Code rules
├── src/            # Evaluation/integration logic
├── images/         # UI and project assets
└── requirements.txt
```

## Technology

`Python` · `Streamlit` · `Open Policy Agent (OPA)` · `Rego` · `JSON`

## Research Context

InspectR is developed as part of an MSc thesis at the University of Oslo in collaboration with SINTEF and the EU-funded DataPACT project.

**Thesis:** *Architecting a Compliance Engine for Multi-Agent Data Pipeline Ecosystems*

> Research prototype — work in progress.
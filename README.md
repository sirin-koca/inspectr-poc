# InspectR

Proof of Concept (PoC)

### Compliance engine for data pipeline ecosystems

InspectR is a research prototype for investigating how regulatory requirements can be operationalized as **Policy-as-Code (PaC)** decoupled from the application logic and evaluated against data pipeline blueprints before deployment.

The current proof of concept uses the **Trondheim Kommune (TK) use case** and selected provisions of the **EU AI Act** to demonstrate the approach.

## Core Architecture - two-input decision mechanism

The pipeline provides facts/evidence, Rego defines the encoded compliance rules where policy provides the condition, and OPA evaluates the two.

![Architecture diagram](https://github.com/user-attachments/assets/b5a0fdb4-8da4-4e42-b50c-b0fb126dc812)
![Architecture diagram](https://github.com/user-attachments/assets/f8edb06e-723b-495f-ab9b-33f7d579591d)

### System evidence ↔ Executable policy ↔ Independent decision engine
<img alt="image" src="https://github.com/user-attachments/assets/2dbd93ad-39a0-4823-8437-b8a6dc1e5143" />


## Repository Structure

```text
inspectr-poc/
├── app.py          # Streamlit application
├── data/           # Pipeline blueprints and supporting data
├── pages/          # InspectR interface and subpages, taxonomy
├── policies/       # Rego Policy-as-Code rules
├── src/            # Evaluation/integration logic
├── images/         # UI and project assets
└── requirements.txt
```

## Technology

`Python` · `JSON` · `PaC` · `Open Policy Agent (OPA)` · `Rego` · `inLUMEN`

## Research Context

InspectR is developed as part of an MSc thesis at the University of Oslo in collaboration with SINTEF and the EU-funded DataPACT project.

**Thesis:** *Architecting a Compliance Engine for Multi-Agent Data Pipeline Ecosystems*

> Research prototype — work in progress.

---

sirin-koca

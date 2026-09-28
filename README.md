# InspectR
_Proof of Concept (PoC)_

### Compliance Analysis Engine for AI/Data Pipelines

> Compliance means satisfying conditions defined by organisational policies derived from laws and regulations, such as the GDPR or AIA.

**Thesis title:** *Architecting a Compliance Engine for Multi-Agent Data Pipeline Ecosystems using Policy-as-Code*

InspectR is a design‑time compliance engine that operationalizes regulatory requirements (GDPR / AIA) as Policy‑as‑Code, by utilizing decoupled OPA/Rego rules to statically assess pipeline blueprints and outputs machine‑readable governance results pre‑deployment.

InspectR investigates how regulatory requirements can be operationalised into traceable, evidence-bound, machine-checkable design-time policies—and where that automation stops.

### TK UC PoC 
This PoC uses the **Trondheim Kommune (TK) use case** and selected provisions of the **GDPR** to demonstrate the approach.The PoC evaluates a static **inLUMEN TK pipeline blueprint** directly against independently defined **Rego policies** using **Open Policy Agent (OPA)**.

```text
Law / Regulatory Requirements (GDPR, AIA)
        ↓
TK UC Obligations (Organisational Policy)
        ↓
Define what observable evidence would support evaluating that policy
        ↓
Design inLUMEN pipeline blueprint with required evidence representations
        ↓
Define the Rego rule that evaluates that evidence and Encode Rego Rules Policy-as-Code
        ↓
Open Policy Agent (OPA) Engine Evaluation
        ↓
OK / FAIL / HUMAN
        ↓
Evidence · Reason · Rule Reference · Remedy
```
### Components

1. **Pipeline blueprint = EVIDENCE**

   The inLUMEN JSON contains the design-time facts InspectR can inspect.

2. **Organisational policy = CONDITION / REQUIREMENT**

   It defines what evidence is expected and what should count as acceptable, unacceptable, or insufficient.

3. **Rego = EXECUTABLE REPRESENTATION OF THAT POLICY**

   The organisational policy conditions are encoded as machine-executable Rego rules.

4. **OPA = EVALUATOR**

   OPA takes:

   ```text
   Pipeline blueprint (evidence)
           +
   Rego rules (encoded policy)
           ↓
        evaluates
           ↓
   OK / FAIL / HUMAN
   ```

5. **InspectR = COMPLIANCE ENGINE around this process**

   InspectR supplies the blueprint and Rego policy to OPA and presents the resulting **status + evidence + reason + rule reference + remedy**.

![Architecture diagram](https://github.com/user-attachments/assets/b5a0fdb4-8da4-4e42-b50c-b0fb126dc812)
![Architecture diagram](https://github.com/user-attachments/assets/f8edb06e-723b-495f-ab9b-33f7d579591d)

### Technology
`Python` · `Plotly` · `Pandas` · `JSON` · `PaC` · `Open Policy Agent (OPA)` · `Rego` · `inLUMEN`

### Repository Structure

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

### Scientific contribution
InspectR demonstrates an architecture and operational method for translating organisational policies into explainable Policy-as-Code controls over static data-pipeline blueprints.

The contribution can be evaluated through:

- separation of policy from application logic;
- independent OPA/Rego decision evaluation;
- explicit evidence requirements;
- traceability from requirement to executable rule;
- distinction between OK, FAIL, and HUMAN;
- conservative treatment of missing or ambiguous evidence;
- applicability to pipeline design before execution;
- use of a realistic municipal data-sharing case.

### Disclaimer
This is a research prototype. InspectR does not certify compliance, determine legal compliance as a whole, encode legal text directly, replace legal interpretation, or execute the pipeline. Results are correct only relative to the explicitly encoded operational policy and available blueprint evidence.

InspectR is an independent, standalone, generic policy engine. This repository showcases only a specific use case (TK use case). The PoC is designed to demonstrate the feasibility of the approach without the complexity of a full implementation. During this PoC implementation of InspectR WE WILL NOT USE IR (the graph model, the Intermediate Representation) for KISS purposes.

InspectR is developed as part of an MSc thesis at the University of Oslo in collaboration with SINTEF and the EU-funded DataPACT project.

> _Research prototype — work in progress_

---

sirin-koca

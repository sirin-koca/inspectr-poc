# InspectR
_Proof of Concept (PoC)_

### Compliance Analysis Engine for AI/Data Pipelines

> Compliance means satisfying conditions defined by organisational policies derived from laws and regulations, such as the GDPR or AIA.

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

### Technology
`Python` · `Plotly` · `Pandas` · `JSON` · `PaC` · `Open Policy Agent (OPA)` · `Rego` · `inLUMEN`

### Research Context

InspectR is developed as part of an MSc thesis at the University of Oslo in collaboration with SINTEF and the EU-funded DataPACT project.

**Thesis:** *Architecting a Compliance Engine for Multi-Agent Data Pipeline Ecosystems using Policy-as-Code*

> _Research prototype — work in progress_

---

sirin-koca

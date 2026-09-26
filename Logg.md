# InspectR Review Summary 260926

The review identified several logical, technical, and functional weaknesses in the InspectR proof of concept. The most important corrected issue concerned the interpretation of human-oversight evidence under AIA-14.

The policy previously treated two fundamentally different situations as the same:

- Human oversight was explicitly disabled.
- No human-oversight information was provided.

These cases have different compliance meanings and must not produce the same result. The Rego policy has now been updated to distinguish them correctly.

## Issue fixed: incorrect AIA-14 classification

### What was wrong

In [`policies/policy.rego`](policies/policy.rego), the policy used:

```rego
object.get(ext, "human_oversight", false) != true
```

This expression uses `false` as the default value when the field is absent. As a result, both of the following inputs evaluated identically:

```json
{
  "human_oversight": false
}
```

and:

```json
{}
```

The policy then returned `HUMAN` in both cases.

### Why this was wrong

The two cases represent different evidence states:

| Blueprint evidence | Meaning | Correct result |
|---|---|---|
| `human_oversight: true` | Oversight is explicitly represented | `OK` |
| `human_oversight: false` | Oversight is explicitly disabled or absent | `FAIL` |
| Field missing | The blueprint does not provide enough information | `HUMAN` |

An explicit `false` is negative evidence. It indicates that the required oversight mechanism is not present. This is different from an absent field, where the system cannot reliably determine whether oversight exists.

Treating both cases as `HUMAN` weakened the evaluation because an explicitly non-compliant component could be presented as merely requiring manual review.

### How it was fixed

The policy now uses a `null` default:

```rego
object.get(ext, "human_oversight", null) == null
```

This allows the policy to detect that the field is genuinely missing.

A separate rule identifies explicit negative evidence:

```rego
object.get(ext, "human_oversight", null) == false
```

The AIA-14 evaluation now follows this order:

1. If any automated decision-support component explicitly has `human_oversight: false`, return `FAIL`.
2. Otherwise, if the field is missing, return `HUMAN`.
3. Otherwise, return `OK`.

### Result after the fix

The bundled extended blueprint contains:

```json
"automated_decision_support": true,
"human_oversight": false
```

It now correctly produces:

```text
AIA-14 — FAIL
Component: prepare_sharing_decision
```

The policy also reports the affected component in the evidence:

```json
{
  "components_without_oversight": [
    "prepare_sharing_decision"
  ]
}
```

## Other issues identified during the review

The following issues were found but were not changed as part of the focused AIA-14 correction.

### 1. OPA executable path is machine-specific

In [`src/evaluator.py`](src/evaluator.py), OPA is invoked using:

```python
C:\Tools\OPA\opa.exe
```

This makes the evaluator dependent on one specific Windows installation path. The application will fail on another machine unless OPA exists at exactly that location.

The error message says that OPA should be available on `PATH`, but the implementation does not actually search `PATH`.

**Recommended improvement:** Resolve OPA through configuration or `PATH`, with an optional environment-variable override.

### 2. The policy path is relative to the current working directory

The evaluator uses:

```python
POLICY_PATH = Path("policies/policy.rego")
```

This works only when Streamlit is launched from the repository root. If the application is started from another directory, the policy may not be found.

**Recommended improvement:** Build the policy path relative to the project or evaluator module location instead of the process working directory.

### 3. `pandas` is missing from the dependency file

[`pages/taxonomy.py`](pages/taxonomy.py) imports pandas, but [`requirements.txt`](requirements.txt) does not declare it.

A clean installation using the requirements file may therefore fail when the Taxonomy page is opened.

**Recommended improvement:** Add:

```text
pandas
```

to the dependency file.

### 4. Blueprint and policy schema are not fully aligned

The standard bundled blueprint [`data/inlumen-tk-uc.json`](data/inlumen-tk-uc.json) does not contain the `compliance_extensions` fields expected by the policy.

Consequently, the policy interprets the standard blueprint as lacking:

- Logging evidence
- Data-source provenance
- Source approval
- Human-oversight evidence

This may be intentional for demonstrating insufficient evidence, but the distinction is not clearly communicated in the interface.

**Recommended improvement:** Document the difference between:

- A raw inLUMEN blueprint
- An enriched compliance blueprint
- A blueprint with explicit non-compliant evidence

## Validation performed

The corrected policy was validated with OPA:

- Rego syntax check: passed
- Extended blueprint evaluation: passed
- Explicit `human_oversight: false`: correctly classified as `FAIL`
- Missing `human_oversight`: remains classified as `HUMAN`
- Python compilation: passed
- JSON data validation: passed
- Diff consistency check: passed

## Final decision rationale

The correction follows a conservative evidence model:

- Positive evidence can support `OK`.
- Explicit negative evidence must produce `FAIL`.
- Missing or ambiguous evidence should produce `HUMAN`.

This preserves the project's stated principle that InspectR should not claim compliance when the evidence is insufficient, while also ensuring that explicit violations are not incorrectly downgraded to an indeterminate result.

---

**Current Worktree**

Three source files are modified and unstaged:

- `policy.rego`
- `inspectr_taxonomy.json`
- `taxonomy.py`

No other application files were changed.

**What Changed**

`policy.rego` no longer evaluates EU AI Act rules. It now evaluates the TK/MUNDAT pipeline against five design-time rules:

| Rule | Purpose |
|---|---|
| `TK-STRUCT-01` | Checks the seven required TK stages and their graph connections. |
| `TK-DATA-01` | Checks source identifiers and approval status. |
| `TK-TRACE-01` | Checks `has_logging: true` on every node. |
| `TK-RISK-01` | Checks that `run_compliance_checks` exists. |
| `TK-HUMAN-01` | Checks human review evidence before sharing. |

The structure rule checks connections by node IDs, not the order of the JSON `nodes` array. This avoids falsely rejecting valid inLUMEN exports whose nodes are serialized in reverse order.

Human-review behavior is:

- `human_oversight: true` → `OK`
- `human_oversight: false` → `FAIL`
- missing `human_oversight` → `HUMAN`

`inspectr_taxonomy.json` now contains:

- TK pipeline structure;
- MUNDAT data-source provenance;
- DPIA and risk assessment;
- logging and traceability;
- human review before sharing.

Each new executable constraint includes a `rule_id` and `evidence_fields`.

`taxonomy.py` was updated to display TK rule IDs and evidence fields. It no longer displays AIA-specific metadata, and its `st.set_page_config()` call now occurs before other Streamlit commands.

**Current Application Logic**

The application starts in `app.py`.

It:

1. Configures Streamlit.
2. Initializes session state:
   - `blueprint`
   - `blueprint_filename`
   - `evaluation_results`
3. Registers the application pages.
4. Displays the DataPACT logo and global footer.
5. Runs the selected page using `pg.run()`.

The main executable workflow is `evaluation.py`:

1. User uploads a JSON blueprint.
2. The file is parsed with Python’s `json` module.
3. The blueprint is stored in Streamlit session state.
4. User presses `Run InspectR`.
5. `src.evaluator.evaluate()` is called.
6. OPA evaluates `data.inspectr.results`.
7. Results are displayed as `OK`, `FAIL`, or `HUMAN`.
8. Each result exposes its reason, evidence, and remedy.

There is still no Intermediate Representation. The uploaded blueprint is passed directly to Rego.

**Core Components**

- `app.py`: application entry point, navigation, session state, global layout.
- `evaluator.py`: Python-to-OPA integration and result validation.
- `policy.rego`: TK/MUNDAT executable rules.
- `inspectr_taxonomy.json`: machine-readable taxonomy.
- `evaluation.py`: blueprint upload and evaluation workflow.
- `taxonomy.py`: Plotly taxonomy visualization.
- data/: raw, extended, non-compliant, and alternative blueprint files.
- assets/: supplementary rule catalog, currently not used by the runtime.
- images/: diagrams, logos, and page assets.
- tk-uc/: TK use-case documentation, inLUMEN export, provenance, and source documents.

Registered pages include:

- Main
- Overview
- Engineering PaC
- The Semantic Gap
- Use Case
- Research
- Taxonomy
- Architecture
- Evaluation
- Test

`aia_subset.py` exists but is not registered in navigation.

**Current Policy Execution**

The evaluator in `evaluator.py`:

1. Requires the input to be a dictionary.
2. Requires `pipeline` to be an object.
3. Requires `pipeline.nodes` to be a list.
4. Invokes OPA using the hard-coded path `opa.exe`.
5. Loads `policy.rego`.
6. Queries `data.inspectr.results`.
7. Parses the OPA JSON response.
8. Validates that every result contains:
   - `rule`
   - `status`
   - `legal_reference`
   - `reason`
   - `evidence`
   - `remedy`
9. Returns the results to Streamlit.

**Observed Blueprint Results**

The current policy was tested against all bundled blueprints:

| Blueprint | Result |
|---|---|
| `inlumen-tk-uc-extended.json` | Structure OK, provenance OK, logging OK, risk OK, human review FAIL |
| `inlumen-tk-uc-non-compliant.json` | Structure OK, provenance OK, logging FAIL, risk OK, human review FAIL |
| `inlumen-tk-uc.json` | Structure OK, provenance FAIL, logging FAIL, risk OK, human review HUMAN |
| `tk_extended_blueprint.json` | Structure OK, provenance FAIL, logging OK, risk OK, human review HUMAN |

The extended blueprint is therefore structurally valid and contains the expected compliance metadata, but explicitly declares that human oversight is disabled.

**Validation Status**

Passed:

- Rego syntax validation with OPA.
- Taxonomy JSON parsing.
- Python compilation for edited pages and core application files.
- Runtime evaluation of all bundled blueprints.

**Current Limitations**

The app is functional as a PoC, but several limitations remain:

- OPA must exist at `opa.exe`.
- The policy path is relative to the current working directory.
- The evaluator does not validate connections, node fields, or schema versions before invoking Rego.
- Evaluation only accepts uploaded files; there is no built-in blueprint selector.
- Results are reset based on filename rather than file content.
- The evaluation page still contains the text `AIA provision`, although the executable policy is now TK/MUNDAT-specific.
- Several explanatory pages still describe the earlier AIA-oriented PoC.
- The old `TK.PipelineStructure` and `TK.ComplianceRequirements` taxonomy branches remain alongside the new `TK.MUNDATRequirements` branch.
- The policy checks design-time declarations only. It does not prove that the actual data processing, DPIA, anonymization, approval, or sharing operations occur at runtime.

**Overall Status**

The app currently works as a **TK/MUNDAT design-time pipeline inspection PoC**:

```text
inLUMEN JSON blueprint
        |
        v
Python evaluator
        |
        v
OPA + TK/MUNDAT Rego policy
        |
        v
OK / FAIL / HUMAN results
        |
        v
Streamlit evidence and remedy display
```

It now evaluates the TK use-case structure and declared compliance evidence rather than presenting the TK use case as an EU AI Act evaluation.



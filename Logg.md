# InspectR Review Summary 260926

## Executive summary

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

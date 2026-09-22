import json
from pathlib import Path
from typing import Any


RULESET_PATH = Path("data/aia_poc_rules.json")


def load_ruleset() -> dict:
    """Load the machine-readable InspectR Policy-as-Code ruleset."""
    with open(RULESET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def find_values(obj: Any, key: str, path: str = "$") -> list[dict]:
    """
    Recursively search the uploaded JSON blueprint for a key.

    No IR is created. InspectR inspects the blueprint directly.
    """

    matches = []

    if isinstance(obj, dict):
        for current_key, value in obj.items():

            current_path = f"{path}.{current_key}"

            if current_key == key:
                matches.append({
                    "path": current_path,
                    "value": value,
                })

            matches.extend(
                find_values(
                    value,
                    key,
                    current_path,
                )
            )

    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            matches.extend(
                find_values(
                    item,
                    key,
                    f"{path}[{index}]",
                )
            )

    return matches


def collect_evidence(
    blueprint: dict,
    evidence_fields: list[str],
) -> dict:
    """Collect observable evidence directly from the blueprint."""

    evidence = {}

    for field in evidence_fields:
        matches = find_values(blueprint, field)

        if matches:
            evidence[field] = matches

    return evidence


def first_boolean(evidence: dict, field: str):
    """
    Return the first explicit boolean value for an evidence field.
    None means the blueprint does not provide deterministic evidence.
    """

    matches = evidence.get(field, [])

    for match in matches:
        value = match["value"]

        if isinstance(value, bool):
            return value

    return None


# =========================================================
# ARTICLE 5(1)(c)
# =========================================================

def evaluate_social_scoring(
    blueprint: dict,
    rule: dict,
) -> dict:

    evidence = collect_evidence(
        blueprint,
        rule["evidence_fields"],
    )

    evaluates_people = first_boolean(
        evidence,
        "evaluates_natural_persons",
    )

    basis = first_boolean(
        evidence,
        "based_on_social_behaviour_or_personal_characteristics",
    )

    social_score = first_boolean(
        evidence,
        "social_score",
    )

    detrimental = first_boolean(
        evidence,
        "detrimental_or_unfavourable_treatment",
    )

    unrelated_context = first_boolean(
        evidence,
        "unrelated_context",
    )

    disproportionate = first_boolean(
        evidence,
        "unjustified_or_disproportionate_treatment",
    )

    # Explicit evidence that the relevant social-scoring mechanism
    # is absent.
    if social_score is False:
        status = "OK"
        reason = (
            "The blueprint explicitly indicates that social scoring "
            "is not used."
        )

    # Article 5(1)(c) requires the social-score mechanism together
    # with the relevant evaluation basis and prohibited treatment.
    elif (
        evaluates_people is True
        and basis is True
        and social_score is True
        and detrimental is True
        and (
            unrelated_context is True
            or disproportionate is True
        )
    ):
        status = "FAIL"
        reason = (
            "The blueprint contains evidence matching the encoded "
            "conditions for prohibited social scoring."
        )

    else:
        status = "HUMAN"
        reason = (
            "The blueprint does not provide sufficient explicit evidence "
            "to determine whether all encoded conditions of Article "
            "5(1)(c) are satisfied."
        )

    return build_result(
        rule,
        status,
        evidence,
        reason,
    )


# =========================================================
# ARTICLE 5(1)(g)
# =========================================================

def evaluate_biometric_categorisation(
    blueprint: dict,
    rule: dict,
) -> dict:

    evidence = collect_evidence(
        blueprint,
        rule["evidence_fields"],
    )

    biometric_categorisation = first_boolean(
        evidence,
        "biometric_categorisation",
    )

    biometric_data = first_boolean(
        evidence,
        "uses_biometric_data",
    )

    sensitive_inference = first_boolean(
        evidence,
        "infers_sensitive_attributes",
    )

    if biometric_categorisation is False:
        status = "OK"
        reason = (
            "The blueprint explicitly indicates that biometric "
            "categorisation is not used."
        )

    elif (
        biometric_categorisation is True
        and biometric_data is True
        and sensitive_inference is True
    ):
        status = "FAIL"
        reason = (
            "The blueprint contains evidence of biometric "
            "categorisation involving inference of sensitive attributes."
        )

    else:
        status = "HUMAN"
        reason = (
            "The blueprint does not provide sufficient explicit evidence "
            "to determine whether the encoded biometric categorisation "
            "prohibition applies."
        )

    return build_result(
        rule,
        status,
        evidence,
        reason,
    )


# =========================================================
# RESULT
# =========================================================

def build_result(
    rule: dict,
    status: str,
    evidence: dict,
    reason: str,
) -> dict:

    return {
        "rule_id": rule["rule_id"],
        "rule": rule["name"],
        "status": status,
        "legal_reference": rule["legal_reference"],
        "taxonomy_constraint": rule["taxonomy_constraint"],
        "evidence": evidence,
        "reason": reason,
        "remedy": (
            rule["remedy"]
            if status == "FAIL"
            else None
        ),
    }


# =========================================================
# INSPECTR ENGINE
# =========================================================

def evaluate(blueprint: dict) -> list[dict]:
    """
    Run InspectR directly against the uploaded JSON blueprint.

    No Intermediate Representation is created.
    """

    ruleset = load_ruleset()

    results = []

    for rule in ruleset["rules"]:

        rule_type = rule["evaluation"]["type"]

        if rule_type == "social_scoring_prohibition":
            result = evaluate_social_scoring(
                blueprint,
                rule,
            )

        elif rule_type == "biometric_sensitive_categorisation":
            result = evaluate_biometric_categorisation(
                blueprint,
                rule,
            )

        else:
            result = {
                "rule_id": rule["rule_id"],
                "rule": rule["name"],
                "status": "HUMAN",
                "legal_reference": rule["legal_reference"],
                "taxonomy_constraint": rule["taxonomy_constraint"],
                "evidence": {},
                "reason": (
                    "No evaluator is implemented for this rule type."
                ),
                "remedy": None,
            }

        results.append(result)

    return results


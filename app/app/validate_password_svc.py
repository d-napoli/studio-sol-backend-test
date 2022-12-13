from app.validation_classes import MinSize, MinUppercase, MinLowercase, MinDigit, MinSpecialChars, NoRepeted
from django.core.exceptions import ValidationError


def _get_rule_validator(rule):
    match rule:
        case "minSize":
            return MinSize()
        case "minUppercase":
            return MinUppercase()
        case "minLowercase":
            return MinLowercase()
        case "minDigit":
            return MinDigit()
        case "minSpecialChars":
            return MinSpecialChars()
        case "noRepeted":
            return NoRepeted()
        case _:
            raise ValidationError(f"Rule {rule} não existe")


def get_no_matches_in_password(password: str, rules) -> list:
    no_matches = []

    for rule in rules:
        rule_name = str(rule.rule)
        rule_value = rule.value
        result = _get_rule_validator(rule_name).validate(password=password, value=rule_value)

        if not result:
            no_matches.append(rule_name)

    return no_matches

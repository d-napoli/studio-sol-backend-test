from pydantic import BaseModel
from enum import Enum


class RulesOptions(str, Enum):
    MIN_SIZE = "minSize"
    MIN_UPPERCASE = "minUppercase"
    MIN_LOWERCASE = "minLowercase"
    MIN_DIGIT = "minDigit"
    MIN_SPECIAL_CHARS = "minSpecialChars"
    NO_REPETED = "noRepeted"

    def __str__(self):
        return self.value


class RulesForm(BaseModel):
    rule: RulesOptions
    value: int


class VerifyPasswordForm(BaseModel):
    password: str
    rules: list[RulesForm]

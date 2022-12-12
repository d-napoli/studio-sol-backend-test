from pydantic import BaseModel
from enum import Enum


class RulesOptions(str, Enum):
    MINSIZE = "minSize"
    MINUPPERCASE = "minUppercase"
    MINLOWERCASE = "minLowercase"
    MINDIGIT = "minDigit"
    MINSPECIALCHARS = "minSpecialChars"
    NOREPETED = "noRepeted"


class RulesForm(BaseModel):
    rule: RulesOptions
    value: int


class VerifyPasswordForm(BaseModel):
    password: str
    rules: list[RulesForm]

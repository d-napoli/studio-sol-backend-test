from abc import ABC, abstractclassmethod
import re


class ValidatePassword(ABC):
    @abstractclassmethod
    def validate(self, password: str, value: int):
        pass


class MinSize(ValidatePassword):
    def validate(self, password: str, value: int):
        return len(password) >= value


class MinUppercase(ValidatePassword):
    def validate(self, password: str, value: int):
        all_uppercases_letters = re.findall("[A-Z]", password)
        qtd_uppercases = len(all_uppercases_letters)

        return qtd_uppercases >= value


class MinLowercase(ValidatePassword):
    def validate(self, password: str, value: int):
        all_lowercase_letters = re.findall("[a-z]", password)
        qtd_lowercases = len(all_lowercase_letters)

        return qtd_lowercases >= value


class MinDigit(ValidatePassword):
    def validate(self, password: str, value: int):
        all_digits = re.findall("[0-9]", password)
        qtd_digits = len(all_digits)

        return qtd_digits >= value


class MinSpecialChars(ValidatePassword):
    def validate(self, password: str, value: int):
        all_special_chars = re.findall("[!@#$%^&*\(\)\-+\\\/\{\}\[\]]", password)
        qtd_special_chars = len(all_special_chars)

        return qtd_special_chars >= value


class NoRepeted(ValidatePassword):
    def validate(self, password: str, value: int = 0):
        if value == 0:
            return True

        is_valid = True

        for index, char in enumerate(password):
            if index != 0 and char == password[index - 1]:
                is_valid = False
                break

        return is_valid

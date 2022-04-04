#!/usr/bin/env python3

import regex
from dataclasses import dataclass


@dataclass
class UserDataValidator:
    name: str
    surname: str
    phone: str
    code: str
    city: str

    def validate_name(self):
        res = regex.findall(r"^\p{Lu}", self.name)
        return bool(res)

    def validate_surname(self):
        res = regex.findall(r"^\p{Lu}", self.surname)
        return bool(res)

    def validate_phone(self):
        res = regex.findall(r"^\(61\)\s\d{3}-\d{2}-\d{2}$", self.phone)
        return bool(res)

    def validate_code(self):
        res = regex.findall(r"^\d{2}-\d{3}$", self.code)
        return bool(res)

    def validate_city(self):
        res = regex.findall(r"^\p{Lu}", self.city)
        return bool(res)


if __name__ == "__main__":
    args = {
        "name": "Miłosz",
        "surname": "Chodkowski",
        "phone": "(61) 223-25-65",
        "code": "61-289",
        "city": "Poznań",
    }
    checker = UserDataValidator(**args)
    print(f"Name valid?: {checker.validate_name()}")
    print(f"Surname valid?: {checker.validate_surname()}")
    print(f"Phone valid?: {checker.validate_phone()}")
    print(f"Code valid?: {checker.validate_code()}")
    print(f"City valid?: {checker.validate_city()}")

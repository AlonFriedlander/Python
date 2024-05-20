from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    age: int
    gender: str

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

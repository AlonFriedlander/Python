import sys
from typing import Optional, Dict, Any, List, Union
from animals.animal import Animal
from log.logging_config import logger
from animals.lion import Lion
from animals.rabbit import Rabbit
from animals.goat import Goat
import json


class Zoo:
    def __init__(self):
        self.config: Dict[str, Any] = Zoo.load_config()
        self.animals: List[Animal] = []

    @staticmethod
    def load_config(config_file: str = "animal_config.json") -> Dict[str, Any]:
        """Loads the animal configuration from a JSON file."""
        try:
            with open(config_file) as f:
                return json.load(f)
        except FileNotFoundError as e:
            logger.error(f"error {e} - use default configurations")
            print("Config file not found. Using default configurations.", file=sys.stderr)
            return {
                "Lion": {"attributes": ["name", "age", "gender"]},
                "Rabbit": {"attributes": ["name", "age", "gender", "fur_color"]}
            }

    def add_new_animal(self, animal_type: str, animal_info: dict) -> bool:
        """Adds a new animal to the zoo."""
        try:
            animal_class = globals()[animal_type]
            animal = animal_class(**animal_info)
            self.animals.append(animal)
            return True
        except KeyError as e:
            logger.error(f"error {e}")
            return False

    def get_all_animals_info(self) -> List[str]:
        """Returns information about all animals in the zoo as a list of strings."""
        animals_info = []
        if not self.animals:
            animals_info.append("No animals in the zoo.")
        else:
            animals_info.append("All animals in the zoo:")
            for index, animal in enumerate(self.animals, start=1):
                animal_type = type(animal).__name__
                animal_info = f"{animal_type} {index}: {animal.get_info()}"
                animals_info.append(animal_info)
        return animals_info

    def get_oldest_animal_info(self) -> Optional[str]:
        """Returns information about the oldest animal in the zoo."""
        if not self.animals:
            return None

        oldest_animal = max(reversed(self.animals), key=lambda animal: animal.age)
        animal_type = type(oldest_animal).__name__
        return f"The oldest animal is from type {animal_type} with info:\n{oldest_animal.get_info()}"

    def count_animals(self, animal_type: Optional[str] = None) -> Union[int, Dict[str, int]]:
        """Counts the number of animals in the zoo, optionally by animal type."""
        animal_count: Union[int, Dict[str, int]] = {}
        if animal_type:
            return sum(1 for animal in self.animals if type(animal).__name__ == animal_type)
        else:
            for animal in self.animals:
                animal_type = type(animal).__name__
                animal_count[animal_type] = animal_count.get(animal_type, 0) + 1
        return animal_count

    def print_number_of_animals(self) -> Dict[str, int]:
        """Returns the number of animals in the zoo, grouped by type."""
        animal_count = self.count_animals()
        total_animals = sum(animal_count.values())
        result = {"Total animals": total_animals}
        for animal_type, count in animal_count.items():
            result[animal_type] = count
        return result

    def collect_animal_info(self) -> Dict[str, Dict[str, Any]]:
        """Collects information about all animals in the zoo."""
        animal_info: Dict[str, Dict[str, Any]] = {}
        for animal in self.animals:
            animal_type = type(animal).__name__
            if animal_type not in animal_info:
                animal_info[animal_type] = {"attributes": []}
            attributes = {}
            for attr, value in animal.__dict__.items():
                attributes[attr] = value
            animal_info[animal_type]["attributes"].append(attributes)
        return animal_info

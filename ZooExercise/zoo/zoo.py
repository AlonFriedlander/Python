#####################
#title: Zoo Module
#author: Alon Friedlander
#description: Module containing the Zoo class for managing animals in a zoo.
#####################

import sys
from dataclasses import asdict
from typing import Optional, Dict, Any, List, Union
from animals.animal import Animal
from log.logging_config import logger
from animals.lion import Lion
from animals.rabbit import Rabbit
from animals.goat import Goat
import json


class Zoo:
    def __init__(self):
        self._config: Dict[str, Any] = Zoo.load_config()
        self._oldest_animal: Optional[Animal] = None
        self._animals: Dict[str, Dict[str, Union[List[Animal], int]]] = {
            animal_type: {"animals": [], "counter": 0} for animal_type in self._config.keys()
        }

    @property
    def config(self) -> Dict[str, Any]:
        """Getter method for config attribute."""
        return self._config

    @property
    def oldest_animal(self) -> Optional[Animal]:
        """Getter method for oldest_animal attribute."""
        return self._oldest_animal

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
            self._animals[animal_type]["animals"].append(animal)
            self._animals[animal_type]["counter"] += 1

            # Update the oldest animal reference if necessary
            if not self._oldest_animal or animal.age >= self._oldest_animal.age:
                self._oldest_animal = animal

            return True
        except KeyError as e:
            logger.error(f"error {e}")
            return False

    def get_all_animals_info(self) -> List[str]:
        """Returns information about all animals in the zoo as a list of strings."""
        animals_info = []
        for animal_type, animal_group in self._animals.items():
            for index, animal in enumerate(animal_group["animals"], start=1):
                animal_info = f"{animal_type} {index}: {animal.get_info()}"
                animals_info.append(animal_info)
        return animals_info

    def count_animals(self, animal_type: Optional[str] = None) -> Union[int, Dict[str, int]]:
        """Counts the number of animals in the zoo, optionally by animal type."""
        animal_count: Union[int, Dict[str, int]] = {}
        if animal_type:
            return self._animals.get(animal_type, {}).get("counter", 0)
        else:
            for animal_type, animal_group in self._animals.items():
                animal_count[animal_type] = animal_group["counter"]
        return animal_count

    def collect_animal_info(self) -> Dict[str, Dict[str, Any]]:
        """Collects information about all animals in the zoo."""
        animal_info: Dict[str, Dict[str, Any]] = {}

        for animal_type, animal_group in self._animals.items():
            animal_list = animal_group["animals"]
            animal_info[animal_type] = {"attributes": []}
            for animal_instance in animal_list:
                animal_info[animal_type]["attributes"].append(asdict(animal_instance))
        return animal_info

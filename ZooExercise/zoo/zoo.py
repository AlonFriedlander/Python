from typing import Optional, Dict, Any, List, Union
from animals.animal import Animal
import json


class Zoo:
    def __init__(self):
        self.config: Optional[Dict[str, Any]] = None
        self.animals: List[Animal] = []
        self.load_config()

    def load_config(self, config_file: str = "animal_config.json") -> None:
        """Loads the animal configuration from a JSON file."""
        try:
            with open(config_file) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print("Config file not found. Using default configurations.")
            self.config = {
                "Lion": {"attributes": ["name", "age", "gender"]},
                "Rabbit": {"attributes": ["name", "age", "gender", "fur_color"]}
            }

    def add_animal(self, animal: Animal) -> None:
        """Adds a new animal to the zoo."""
        self.animals.append(animal)

    def print_all_animals(self) -> None:
        """Prints information about all animals in the zoo."""
        if not self.animals:
            print("No animals in the zoo.")
        else:
            print("All animals in the zoo:")
            for index, animal in enumerate(self.animals, start=1):
                animal_type = type(animal).__name__
                print(f"{animal_type} {index}:")
                print(animal.get_info())

    def print_oldest_animal_info(self) -> None:
        """Prints information about the oldest animal in the zoo."""
        if not self.animals:
            print("No animals in the zoo.")
            return

        oldest_animal = max(self.animals, key=lambda animal: animal.age)
        animal_type = type(oldest_animal).__name__
        print(f"The oldest animal is from type {animal_type} with info:")
        print(oldest_animal.get_info())

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

    def print_number_of_animals(self) -> None:
        """Prints the number of animals in the zoo, grouped by type."""
        animal_count = self.count_animals()
        total_animals = sum(animal_count.values())
        print(f"Total animals: {total_animals}")
        for animal_type, count in animal_count.items():
            print(f"{animal_type}: {count}")

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

    def export_to_json_file(self, filename: str = "animal_info.json") -> None:
        """Exports animal information to a JSON file."""
        animal_info = self.collect_animal_info()
        with open(filename, "w") as file:
            json.dump(animal_info, file, indent=4)
        print(f"Animal information successfully exported to {filename}.")


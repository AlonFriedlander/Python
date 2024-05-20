from animals.animal import Animal
import json


class Zoo:
    def __init__(self):
        self.animals = []
        self.load_config()

    def load_config(self, config_file="animal_config.json"):
        try:
            with open(config_file) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print("Config file not found. Using default configurations.")
            self.config = {
                "Lion": {"attributes": ["name", "age", "gender"]},
                "Rabbit": {"attributes": ["name", "age", "gender", "fur_color"]}
            }

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def print_all_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            print("All animals in the zoo:")
            for index, animal in enumerate(self.animals, start=1):
                animal_type = type(animal).__name__
                print(f"{animal_type} {index}:")
                print(animal.get_info())

    def print_oldest_animal_info(self):
        if not self.animals:
            print("No animals in the zoo.")
            return

        oldest_animal = max(reversed(self.animals), key=lambda animal: animal.age)

        print("Information of the oldest animal:")
        print(oldest_animal.get_info())

    def print_number_of_animals(self):
        num_animals = len(self.animals)
        print(f"Number of animals currently in the zoo: {num_animals}")

    def collect_animal_info(self):
        animal_info = {}
        for animal in self.animals:
            animal_type = type(animal).__name__
            if animal_type not in animal_info:
                animal_info[animal_type] = {"attributes": []}
            attributes = {}
            for attr, value in animal.__dict__.items():
                attributes[attr] = value
            animal_info[animal_type]["attributes"].append(attributes)
        return animal_info

    def export_to_json_file(self, filename="animal_info.json"):
        animal_info = self.collect_animal_info()
        with open(filename, "w") as file:
            json.dump(animal_info, file, indent=4)
        print(f"Animal information successfully exported to {filename}.")
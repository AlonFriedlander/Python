import json
from typing import Dict
from collections import namedtuple

from zoo.zoo import Zoo
from animals.lion import Lion
from animals.rabbit import Rabbit
from animals.goat import Goat

MenuItem = namedtuple("MenuItem", ["function", "print_statement"])


class ZooCLI:
    def __init__(self, zoo: Zoo):
        self.zoo = zoo
        self.running: bool = True
        self.menu_options: Dict[str, MenuItem] = {
            "1": MenuItem(self.add_new_animal, "Add New Animal"),
            "2": MenuItem(self.print_all_animals, "Print All Animals"),
            "3": MenuItem(self.export_to_json_file, "Export to JSON File"),
            "4": MenuItem(self.print_oldest_animal_info, "Print Oldest Animal Info"),
            "5": MenuItem(self.print_number_of_animals, "Print Number of Animals"),
            "6": MenuItem(self.load_animals_from_json, "Load Animals from JSON"),
            "7": MenuItem(self.print_number_of_specific_animal, "Print Number of Specific Animal"),
            "8": MenuItem(self.exit_program, "Exit"),
        }

    def run(self) -> None:
        """Starts the main loop of the program."""
        while self.running:
            self.display_menu()
            choice = input("Enter your choice: ")
            try:
                selected_option = self.menu_options[choice]
                selected_option.function()
            except KeyError:
                print("Invalid choice. Please select a valid option.")

    def display_menu(self) -> None:
        """Displays the menu options."""
        print("MENU")
        for key, item in self.menu_options.items():
            print(f"{key}: {item.print_statement}")

    def exit_program(self) -> None:
        print("Exiting the program. Goodbye!")
        self.running = False
        return

    def add_new_animal(self) -> None:
        """Allows the user to add a new animal to the zoo."""
        print("Select the type of animal:")
        for key, value in self.zoo.config.items():
            print(f"{key}")

        while True:
            try:
                animal_type = input("Enter your choice: ")
                animal_attributes = self.zoo.config[animal_type]["attributes"]
                animal_info = {}

                for attr_info in animal_attributes:
                    attr_name, attr_instructions = next(iter(attr_info.items()))
                    prompt = f"Enter the {attr_instructions} of the {animal_type.lower()}: "
                    validation_func = globals().get(f"is_valid_{attr_name.lower()}")
                    animal_info[attr_name] = get_valid_input(prompt, validation_func)

                animal_class = globals()[animal_type]
                animal = animal_class(**animal_info)
                self.zoo.add_animal(animal)
                print(f"{animal_type} successfully added to the zoo.")
                break
            except KeyError:
                print("Invalid choice. Please select a valid option.")

    def print_all_animals(self) -> None:
        """Prints information about all animals in the zoo."""
        self.zoo.print_all_animals()

    def export_to_json_file(self) -> None:
        """Exports information about all animals to a JSON file."""
        self.zoo.export_to_json_file()

    def print_oldest_animal_info(self) -> None:
        """Prints information about the oldest animal in the zoo."""
        self.zoo.print_oldest_animal_info()

    def print_number_of_animals(self) -> None:
        """Prints the number of animal in the zoo."""
        self.zoo.print_number_of_animals()

    def load_animals_from_json(self) -> None:
        """Loads animals from a JSON file."""
        try:
            file_path = input("Enter the path to the JSON file: ")
            with open(file_path) as f:
                data = json.load(f)

            for animal_type, animal_data in data.items():
                for attributes in animal_data["attributes"]:
                    animal_info = {}

                    # Validate each attribute's value before adding it to animal_info
                    for attr_info in attributes.items():
                        attr_name, attr_value = attr_info
                        validation_func = globals().get(f"is_valid_{attr_name.lower()}")
                        if validation_func is None or not validation_func(attr_value):
                            print(f"Invalid value for {attr_name}: {attr_value}. Skipping animal.")
                            break
                        animal_info[attr_name] = attr_value
                    else:  # If all attributes pass validation, create the animal instance
                        try:
                            animal_class = globals()[animal_type]
                            animal = animal_class(**animal_info)
                            self.zoo.add_animal(animal)
                        except KeyError:
                            print(f"Unknown animal type: {animal_type}")
                            continue

            print("Animals loaded from JSON file successfully.")

        except FileNotFoundError:
            print("Error loading animals from JSON: File not found.")
        except Exception as e:
            print(f"Error loading animals from JSON: {e}")

    def print_number_of_specific_animal(self) -> None:
        """Prints the number of a specific type of animal in the zoo."""
        print("Enter the type of animal to count: ")
        for key, value in self.zoo.config.items():
            print(f"{key}")

        animal_type = input("Enter your choice: ")
        animal_count = self.zoo.count_animals(animal_type)

        if animal_count == 0:
            print(f"No animals of {animal_type} in the zoo.")
        else:
            print(f"Number of {animal_type}s: {animal_count}")


def is_valid_name(name: str) -> bool:
    """Validates the name of an animal."""
    return all(char.isalpha() or char.isspace() for char in name)


def is_valid_age(age: str) -> bool:
    """Validates the age of an animal."""
    try:
        float_age = float(age)
        return 0 <= float_age <= 99
    except ValueError:
        return False


def is_valid_gender(gender: str) -> bool:
    """Validates the gender of an animal."""
    return gender.lower() in ['male', 'female']


def is_valid_fur_color(fur_color: str) -> bool:
    """Validates the fur color of an animal."""
    return fur_color.lower() in ['gray', 'white']


def get_valid_input(prompt: str, validation_func=None) -> str:
    """Gets user input and validates it using the provided validation function."""
    while True:
        user_input = input(prompt)
        try:
            if validation_func is None or validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a valid value.")


if __name__ == "__main__":
    zoo = Zoo()
    cli = ZooCLI(zoo)
    cli.run()

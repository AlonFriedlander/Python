############
#title: ZooCLI Module
#author: Alon Friedlander
#description: Module containing the ZooCLI class for managing a command-line interface for a zoo.
############

import json
import sys
from typing import Dict, Callable
from collections import namedtuple
from log.logging_config import logger
from zoo.zoo import Zoo


MenuItem = namedtuple("MenuItem", ["function", "print_statement"])


def create_validation_functions() -> Dict[str, Callable[[str], bool]]:
    """Creates the validation functions for loading animals from JSON."""
    return {
        "name": is_valid_name,
        "age": is_valid_age,
        "gender": is_valid_gender,
        "fur_color": is_valid_fur_color
    }


class ZooCLI:
    def __init__(self, zoo_object: Zoo):
        self.zoo = zoo_object
        self.running: bool = True
        self.menu_options: Dict[str, MenuItem] = self.create_menu_options()
        self.validation_functions: Dict[str, Callable[[str], bool]] = create_validation_functions()

    def create_menu_options(self) -> Dict[str, MenuItem]:
        """Creates the menu options."""
        return {
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
                logger.info(f"choose '{choice}' from main menu")
                selected_option.function()
            except KeyError:
                print("Invalid choice. Please select a valid option.", file=sys.stderr)
                logger.error(f"Invalid choice '{choice}' in main menu")

    def display_menu(self) -> None:
        """Displays the menu options."""
        print("MENU")
        for key, item in self.menu_options.items():
            print(f"{key}: {item.print_statement}")

    def exit_program(self) -> None:
        """Exits the program, giving the user an option to save data to a JSON file."""
        save_option = input("Do you want to save the data to a JSON file before exiting? (yes/no): ").lower()
        if save_option == 'yes':
            self.export_to_json_file()
            logger.info(f"saving the data before exit")
        print("Exiting the program. Goodbye!")
        self.running = False
        logger.info(f"exit the program")

    def add_new_animal(self) -> None:
        """Allows the user to add a new animal to the zoo."""
        print("Select the type of animal:")
        for key, value in self.zoo.config.items():
            print(f"{key}")

        while True:
            try:
                animal_type = input("Enter your choice: ")
                animal_attributes = self.zoo.config[animal_type]["attributes"]
                logger.info(f"try to add a new '{animal_type}'")
                animal_info = {}

                for attr_info in animal_attributes:
                    attr_name, attr_instructions = next(iter(attr_info.items()))
                    prompt = f"Enter the {attr_instructions} of the {animal_type.lower()}: "
                    validation_func = self.validation_functions.get(attr_name.lower())
                    animal_info[attr_name] = get_valid_input(prompt, validation_func)

                added_successfully = self.zoo.add_new_animal(animal_type, animal_info)
                if added_successfully:
                    print(f"{animal_type} successfully added to the zoo.")
                    logger.info(f"successfully add a new {animal_type} name: '{animal_info.get('name')}'")
                else:
                    print("Failed to add the animal to the zoo.")
                break
            except KeyError:
                print("Invalid choice. Please select a valid option.", file=sys.stderr)
                logger.error(f"invalid choose of type at add new animal")

    def print_all_animals(self) -> None:
        """Prints information about all animals in the zoo."""
        animals_info = self.zoo.get_all_animals_info()
        logger.info(f"print all the animals info")
        for info in animals_info:
            print(info)

    def export_to_json_file(self) -> None:
        """Exports information about all animals to a JSON file."""
        animal_info = self.zoo.collect_animal_info()
        while True:
            try:
                filename = input("Enter the filename for the JSON file: ")
                with open(filename, "w") as file:
                    json.dump(animal_info, file, indent=4)
                print(f"Animal information successfully exported to {filename}.")
                logger.info(f"successfully exported to {filename}")
                break
            except (FileNotFoundError, PermissionError, IOError) as e:
                print(f"Error exporting to JSON file: {e}. Please enter a valid filename.", file=sys.stderr)
                logger.error(f"error at export to json: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}", file=sys.stderr)
                logger.error(f"error at export to json: {e}")

    def print_oldest_animal_info(self) -> None:
        """Prints information about the oldest animal in the zoo."""
        oldest_animal_info = self.zoo.get_oldest_animal_info()
        if oldest_animal_info:
            logger.info(f"print oldest animal {oldest_animal_info}")
            print(oldest_animal_info)
        else:
            print("No animals in the zoo.")

    def print_number_of_animals(self) -> None:
        """Prints the number of animals in the zoo."""
        animal_count = self.zoo.print_number_of_animals()
        logger.info(f"print animal count")
        for animal_type, count in animal_count.items():
            print(f"{animal_type}: {count}")

    def load_animals_from_json(self) -> None:
        """Loads animals from a JSON file."""
        logger.info(f"try to load animals from json")
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
                        validation_func = self.validation_functions.get(attr_name.lower())
                        if validation_func is None or not validation_func(attr_value):
                            print(f"Invalid value for {attr_name}: {attr_value}. Skipping animal.")
                            break
                        animal_info[attr_name] = attr_value
                    else:  # If all attributes pass validation, create the animal instance
                        added_successfully = self.zoo.add_new_animal(animal_type, animal_info)
                        if added_successfully:
                            logger.info(f"successfully add a new {animal_type} name: '{animal_info.get('name')}'")
                        else:
                            print("Failed to add the animal to the zoo.")
            logger.info(f"load animals successfully")
            print("Animals loaded from JSON file successfully.")

        except FileNotFoundError:
            print("Error loading animals from JSON: File not found.", file=sys.stderr)
            logger.error(f"Error loading animals from JSON: File not found.")
        except Exception as e:
            print(f"Error loading animals from JSON: {e}", file=sys.stderr)
            logger.error(f"Error loading animals from JSON: {e}")

    def print_number_of_specific_animal(self) -> None:
        """Prints the number of a specific type of animal in the zoo."""
        print("Enter the type of animal to count: ")
        for key, value in self.zoo.config.items():
            print(f"{key}")

        animal_type = input("Enter your choice: ")
        animal_count = self.zoo.count_animals(animal_type)

        logger.info(f"print number of specific animal")

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
        logger.error(f"function is_valid_age- valueError ")
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
                logger.error(f"invalid input in get_valid_input = {user_input} ")
        except ValueError:
            logger.error(f"function get_valid_input- valueError ")
            print("Invalid input. Please enter a valid value.", file=sys.stderr)


if __name__ == "__main__":
    zoo = Zoo()
    cli = ZooCLI(zoo)
    cli.run()

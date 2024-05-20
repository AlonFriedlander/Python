from zoo.zoo import Zoo
from animals.lion import Lion
from animals.rabbit import Rabbit

from collections import namedtuple

MenuItem = namedtuple("MenuItem", ["function", "print_statement"])


class ZooCLI:
    def __init__(self, zoo: Zoo):
        self.zoo = zoo
        self.menu_options = {
            "1": MenuItem(self.add_new_animal, "Add New Animal"),
            "2": MenuItem(self.print_all_animals, "Print All Animals"),
            "3": MenuItem(self.export_to_json_file, "Export to JSON File"),
            "4": MenuItem(self.print_oldest_animal_info, "Print Oldest Animal Info"),
            "5": MenuItem(self.print_number_of_animals, "Print Number of Animals"),
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            try:
                selected_option = self.menu_options[choice]
                selected_option.function()
            except KeyError:
                print("Invalid choice. Please select a valid option.")

    def display_menu(self):
        print("MENU")
        for key, item in self.menu_options.items():
            print(f"{key}: {item.print_statement}")

    def add_new_animal(self):
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

    def print_all_animals(self):
        self.zoo.print_all_animals()

    def export_to_json_file(self):
        self.zoo.export_to_json_file()

    def print_oldest_animal_info(self):
        self.zoo.print_oldest_animal_info()

    def print_number_of_animals(self):
        self.zoo.print_number_of_animals()


def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)


def is_valid_age(age):
    float_age = float(age)
    return 0 <= float_age <= 99


def is_valid_gender(gender):
    return gender.lower() in ['male', 'female']


def is_valid_fur_color(fur_color):
    return fur_color.lower() in ['gray', 'white']


def get_valid_input(prompt, validation_func=None):
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

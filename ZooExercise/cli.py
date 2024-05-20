from zoo.zoo import Zoo
from animals.lion import Lion
from animals.rabbit import Rabbit


def display_menu():
    print("MENU")
    print("1: Add New Animal")
    print("2: Print All Animals")
    print("3: Export to Text File")


def get_valid_input(prompt, data_type, validation_func=None):
    while True:
        user_input = input(prompt)
        try:
            value = data_type(user_input)
            if validation_func is None or validation_func(value):
                return value
            else:
                print("Invalid input. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)


def is_valid_age(age):
    return 0 <= age <= 99


def is_valid_gender(gender):
    return gender.lower() in ['male', 'female']


def is_valid_fur_color(fur_color):
    return fur_color.lower() in ['gray', 'white']


class ZooCLI:
    def __init__(self, zoo: Zoo):
        self.zoo = zoo
        self.menu_options = {
            "1": self.add_new_animal,
            "2": self.print_all_animals,
            "3": self.export_to_text_file,
        }

    def run(self):
        while True:
            display_menu()
            choice = input("Enter your choice: ")
            if choice in self.menu_options:
                self.menu_options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")

    def add_new_animal(self):
        animal_classes = {"1": Lion, "2": Rabbit}

        print("Select the type of animal:")
        for key, value in animal_classes.items():
            print(f"{key}: {value.__name__.replace('add_', '').capitalize()}")

        while True:
            animal_type = input("Enter your choice: ")
            if animal_type in animal_classes:
                animal = animal_classes[animal_type]()
                self.zoo.add_animal(animal)
                print(f"{animal.__class__.__name__} successfully added to the zoo.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def print_all_animals(self):
        self.zoo.print_all_animals()

    def export_to_text_file(self):
        pass


if __name__ == "__main__":
    zoo = Zoo()
    cli = ZooCLI(zoo)
    cli.run()

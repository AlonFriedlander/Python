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
            "3": MenuItem(self.export_to_text_file, "Export to Text File"),
            "4": MenuItem(self.print_oldest_animal_info, "Print Oldest Animal Info"),
            "5": MenuItem(self.print_number_of_animals, "Print Number of Animals"),
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice in self.menu_options:
                selected_option = self.menu_options[choice]
                selected_option.function()
            else:
                print("Invalid choice. Please select a valid option.")

    def display_menu(self):
        print("MENU")
        for key, item in self.menu_options.items():
            print(f"{key}: {item.print_statement}")

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

    def print_oldest_animal_info(self):
        self.zoo.print_oldest_animal_info()

    def print_number_of_animals(self):
        self.zoo.print_number_of_animals()


if __name__ == "__main__":
    zoo = Zoo()
    cli = ZooCLI(zoo)
    cli.run()

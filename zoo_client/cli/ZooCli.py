############
#title: ZooCLI Module
#author: Alon Friedlander
#description: Module containing the ZooCLI class for managing a command-line interface for a zoo.
############

import json
import socket
import sys
from typing import Dict, Callable
from collections import namedtuple


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
    def __init__(self, server_address):
        self.server_host, self.server_port = server_address
        self.running: bool = True
        self.menu_options: Dict[str, MenuItem] = self.create_menu_options()
        self.validation_functions: Dict[str, Callable[[str], bool]] = create_validation_functions()

    def send_request(self, request, timeout=5) -> str:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
                client_socket.settimeout(timeout)  # Set a timeout for socket operations
                client_socket.sendto(request.encode(), (self.server_host, self.server_port))
                # print(f"Sent request to server: {request}")
                response, _ = client_socket.recvfrom(1024)
                # print(f"Received response from server: {response.decode()}")
                return response.decode()
        except socket.timeout:
            print("Error: Connection timed out. Please try again later.")
            return ""
        except ConnectionResetError:
            print("Error: The server is not available. Please try again later.")
            return ""

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
                selected_option.function()
            except KeyError:
                print("Invalid choice. Please select a valid option.", file=sys.stderr)

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
        print("Exiting the program. Goodbye!")
        self.running = False

    def add_new_animal(self) -> None:
        """Allows the user to add a new animal to the zoo."""
        try:
            # Request zoo config from the server
            request = json.dumps({"method": "get_config"})
            response = self.send_request(request)

            if response:
                config_data = json.loads(response)
                print("Select the type of animal:")
                for key, value in config_data.items():
                    print(f"{key}")

                while True:
                    try:
                        animal_type = input("Enter your choice: ")
                        animal_attributes = config_data[animal_type]["attributes"]
                        animal_info = {}

                        for attr_info in animal_attributes:
                            attr_name, attr_instructions = next(iter(attr_info.items()))
                            prompt = f"Enter the {attr_instructions} of the {animal_type.lower()}: "
                            validation_func = self.validation_functions.get(attr_name.lower())
                            animal_info[attr_name] = get_valid_input(prompt, validation_func)

                        # Construct request to add new animal
                        request = json.dumps(
                            {"method": "add_new_animal", "args": {
                                "animal_type": animal_type,
                                "animal_info": animal_info}
                             }
                        )
                        response = self.send_request(request)

                        if response:
                            print(f"{animal_type} successfully added to the zoo.")
                        else:
                            print("Failed to add the animal to the zoo.")
                        break
                    except KeyError:
                        print("Invalid choice. Please select a valid option.", file=sys.stderr)
        except json.JSONDecodeError:
            print("Error: Invalid JSON response from server.", file=sys.stderr)

    def print_all_animals(self) -> None:
        """Prints information about all animals in the zoo."""
        try:
            # Construct request to get all animal information
            request = json.dumps({"method": "get_all_animals_info"})

            # Send request to the server and receive response
            response = self.send_request(request)

            if response:
                animals_info = json.loads(response)
                if not animals_info:
                    print("No animals in the zoo.")
                else:
                    for info in animals_info:
                        print(info)
            else:
                print("Failed to get animal information from the server.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON response from server.", file=sys.stderr)

    def export_to_json_file(self) -> None:
        """Exports information about all animals to a JSON file."""
        # Construct request to collect animal information
        request = json.dumps({"method": "collect_animal_info"})
        # Send request to the server and receive response
        response = self.send_request(request)

        # Process the response
        if response:
            try:
                animal_info = json.loads(response)

                # Prompt user for filename
                filename = input("Enter the filename for the JSON file: ")
                with open(filename, "w") as file:
                    json.dump(animal_info, file, indent=4)
                print(f"Animal information successfully exported to {filename}.")
            except (FileNotFoundError, PermissionError, IOError) as e:
                print(f"Error exporting to JSON file: {e}. Please enter a valid filename.", file=sys.stderr)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON response from server: {e}", file=sys.stderr)
        else:
            print("Failed to retrieve information from the server.")

    def print_oldest_animal_info(self) -> None:
        """Prints information about the oldest animal in the zoo."""
        # Construct the request
        request = json.dumps({"method": "get_oldest_animal"})

        # Send the request to the server
        response = self.send_request(request)

        # Process the response
        if response:
            oldest_animal_info = json.loads(response)
            if oldest_animal_info:
                print(f"The oldest animal is {oldest_animal_info}")
            else:
                print("No animals in the zoo.")
        else:
            print("Failed to retrieve information from the server.")

    def print_number_of_animals(self) -> None:
        """Prints the number of animals in the zoo."""
        # Construct request to get all animal information
        request = json.dumps({"method": "count_animals"})
        # Send request to the server and receive response
        response = self.send_request(request)

        # Process the response
        if response:
            animal_count = json.loads(response)
            total_animals = sum(animal_count.values())

            print(f"Total animals: {total_animals}")

            for animal_type, count in animal_count.items():
                print(f"{animal_type} : {count}")
        else:
            print("Failed to retrieve information from the server.")

    # In cli.py
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
                        validation_func = self.validation_functions.get(attr_name.lower())
                        if validation_func is None or not validation_func(attr_value):
                            print(f"Invalid value for {attr_name}: {attr_value}. Skipping animal.")
                            break
                        animal_info[attr_name] = attr_value
                    else:  # If all attributes pass validation, create the animal instance
                        # Construct request to add new animal
                        request = json.dumps({
                            "method": "add_new_animal",
                            "args": {
                                "animal_type": animal_type,
                                "animal_info": animal_info
                            }
                        })
                        # Send request to the server and receive response
                        response = self.send_request(request)
                        if response and response == "success":
                            print("Success to add the animal to the zoo.")
                        else:
                            print("Failed to add the animal to the zoo.")
            print("Animals loaded from JSON file successfully.")

        except FileNotFoundError:
            print("Error loading animals from JSON: File not found.", file=sys.stderr)
        except Exception as e:
            print(f"Error loading animals from JSON: {e}", file=sys.stderr)

    def print_number_of_specific_animal(self) -> None:
        """Prints the number of a specific type of animal in the zoo."""

        # Construct request to get the zoo configuration
        request = json.dumps({"method": "get_config"})
        # Send request to the server and receive response
        response = self.send_request(request)

        # Process the response
        if response:
            config_data = json.loads(response)
            print("Enter the type of animal to count: ")
            for key, value in config_data.items():
                print(f"{key}")
            animal_type = input("Enter your choice: ")

            # Construct request to count animals of a specific type
            request = json.dumps({"method": "count_animals", "args": {"animal_type": animal_type}})
            # Send request to the server and receive response
            response = self.send_request(request)

            # Process the response
            if response:
                animal_count = json.loads(response)
                if animal_count == 0:
                    print(f"No animals of {animal_type} in the zoo.")
                else:
                    print(f"Number of {animal_type}s: {animal_count}")
            else:
                print("Failed to retrieve information from the server.")
        else:
            print("Failed to retrieve zoo configuration from the server.")


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
            print("Invalid input. Please enter a valid value.", file=sys.stderr)


class Animal:
    def __init__(self):
        self.name = get_valid_input("Enter the name (string): ", str, is_valid_name)
        self.age = get_valid_input("Enter the age of the (0-99): ", int, is_valid_age)
        self.gender = get_valid_input("Enter the gender (Male/Female): ", str, is_valid_gender)

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


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




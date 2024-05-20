from animals.animal import Animal


class Zoo:
    def __init__(self):
        self.animals = []

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

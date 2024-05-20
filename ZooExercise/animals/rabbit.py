from animals.animal import Animal

from animals.animal import get_valid_input


class Rabbit(Animal):
    def __init__(self):
        super().__init__()
        self.fur_color = get_valid_input("Enter the fur color of the rabbit (Gray/White): ", str, is_valid_fur_color)

    def get_info(self):
        return super().get_info() + f", Fur Color: {self.fur_color}"


def is_valid_fur_color(fur_color):
    return fur_color.lower() in ['gray', 'white']

from dataclasses import dataclass

from animals.animal import Animal


@dataclass
class Rabbit(Animal):
    fur_color: str

    def get_info(self):
        return super().get_info() + f", Fur Color: {self.fur_color}"

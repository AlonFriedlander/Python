from cli.cli import ZooCLI
from zoo.zoo import Zoo

if __name__ == "__main__":
    zoo = Zoo()
    cli = ZooCLI(zoo)
    cli.run()
    
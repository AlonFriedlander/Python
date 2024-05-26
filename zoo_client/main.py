
from cli.ZooCli import ZooCLI

if __name__ == "__main__":
    server_host = "localhost"
    server_port = 12345
    zoo_cli = ZooCLI((server_host, server_port))
    zoo_cli.run()

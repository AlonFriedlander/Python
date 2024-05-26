import socket
import threading
import queue
import json
from zoo.zoo import Zoo

SERVER_ADDRESS = ('localhost', 12345)

request_queue = queue.Queue()
zoo_instance = Zoo()  # Create a single instance of the Zoo object


def handle_client_requests():
    while True:
        try:
            if not request_queue.empty():
                client_addr, client_port, request_data = request_queue.get()
                # print(f"Received request from {client_addr}:{client_port}: {request_data}")

                # Parse the JSON request data
                try:
                    request = json.loads(request_data.decode())
                    method_name = request.get('method')
                    args = request.get('args', {})
                    # print(args)

                    # Call the method on the single instance of Zoo object
                    method = getattr(zoo_instance, method_name)
                    response_data = method(**args)

                    # print("response data: ")
                    # print(response_data)
                    # Send back the response
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    client_socket.sendto(json.dumps(response_data).encode(), (client_addr, client_port))
                except Exception as e:
                    print("Error processing request:", e)

        except Exception as e:
            print("Error occurred in client request handling:", e)


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(SERVER_ADDRESS)
    # print("Server is listening for client requests...")

    threading.Thread(target=handle_client_requests).start()

    while True:
        data, addr = server_socket.recvfrom(1024)
        request_queue.put((addr[0], addr[1], data))  # Enqueue the request along with client details
        # print(f"Received request from client {addr[0]}:{addr[1]}")

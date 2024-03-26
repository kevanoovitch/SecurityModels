import socket


def send_public_key(client_socket):
    with open('mypublickey.asc', 'r') as keyfile:
        public_key = keyfile.read()
    client_socket.sendall(public_key.encode('utf-8'))


def start_server(port=8080):  # Port 8080 is bad!!!
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)
    print(f"Listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        send_public_key(client_socket)
        client_socket.close()


if __name__ == "__main__":
    start_server()

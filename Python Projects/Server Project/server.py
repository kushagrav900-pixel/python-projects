import socket
# AF_INET: IPv4
# SOCK_STREAM: TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1' # localhost same machine only
PORT = 5555 # pick any free port (1024 - 65535)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}")
client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")
data = client_socket.recv(1024) # reads 1024 bytes of data from the client
message = data.decode('utf-8')
print(f"Received message: {message}")

reply = "Hello, Client! Got your message."
client_socket.send(reply.encode('utf-8'))
client_socket.close()
server_socket.close()
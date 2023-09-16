

from socket import *
from functions import menu


HOST = 'localhost'
PORT = 5000
client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    try:
        menu()
        message = str(input("OPÇÃO: "))

        if(message != None):
            client.send(str.encode(message))
            messageReceive = client.recv(1024)
            print(f"Resposta: {messageReceive.decode()}")

    except ValueError as ex:
        print("Erro: Escolha uma opção válida!!!")
    except ConnectionError as ex:
        print("Erro: Não foi possível se conectar ao servidor.")
    except TimeoutError as ex:
        print("Erro: O servidor não respondeu a tempo.")



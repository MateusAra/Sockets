

from socket import *
from functions import file_verify, menu, receave_file


HOST = '127.0.0.1'
PORT = 5000
client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    try:
        menu()
        message = str(input("OPÇÃO: "))

        if message != None:
            if int(message) > 5 or int(message) <= 0:
                raise ValueError
            if message == "3":
                receave_file(message, client)
                continue
            if message == "5":
                print("Fechando conexão com servidor")
                client.close()
                break
            client.send(str.encode(message))
            messageReceive = client.recv(1024)
            print(f"RESPOSTA: {messageReceive.decode()}")

    except ValueError as ex:
        print("Erro: Escolha uma opção válida!!!")
    except ConnectionError as ex:
        print("Erro: Não foi possível se conectar ao servidor.")
    except TimeoutError as ex:
        print("Erro: O servidor não respondeu a tempo.")

from socket import *
from functions import receive_messages, send_messages
import threading


def main():

    HOST = '127.0.0.1'
    PORT = 5000
    client = socket(AF_INET, SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
    except :
        print("Erro: Não foi possível se conectar ao servidor.")

    client_name = input("Nome do Cliente: ")
    print("\nCliente conectado!! Obtendo informações do Servidor")

    thread_send = threading.Thread(target=send_messages, args=[client, client_name] )
    thread_recv = threading.Thread(target=receive_messages, args=[client])

    thread_recv.start()
    thread_send.start()

main()
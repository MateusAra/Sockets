
from time import sleep


def menu():
    print(
        """ 
        _______________________
        |        OPCÕES       |
        |_________:)__________|
        [1] - CONSULTA DADOS: 
        [2] - HORA ATUAL:
        [3] - RECEBER ARQUIVO:
        [4] - LISTAR ARQUIVOS:
        [5] - SAIR:
        """)

def request_file(client_name, client):
    file_name = input("Nome do arquivo: ")
    server_command = str.encode(f"\nCliente:{client_name}\nOpção:3 {file_name}")
    client.send(server_command)
    
def file_verify(file_name, conn):
    option = "4"
    conn.send(option.encode())
    files_exists = conn.recv(10000000).decode()
    if file_name not in files_exists:
        return False
    return True

def send_messages(client, client_name):
    while True:
        try:
            sleep(3)
            menu()
            message = str(input("OPÇÃO: "))

            if message == None:
                continue
            if int(message) > 5 or int(message) <= 0:
                raise ValueError
            
            if message == "3":
                request_file(client_name, client)
                continue

            if message == "5":
                print("Fechando conexão com servidor")
                client.close()
                break
            client.send(f"\nCliente:{client_name}\nOpção:{message}".encode())

        except ValueError as ex:
            print("Erro: Escolha uma opção válida!!!")
        except ConnectionError as ex:
            print("Erro: Não foi possível se conectar ao servidor.")
        except TimeoutError as ex:
            print("Erro: O servidor não respondeu a tempo.")


def receive_messages(client):
    while True:
        try:
            messageReceive = client.recv(4096)
            message_decoded = messageReceive.decode()
            if "file_type" in message_decoded:
                receave_file(message_decoded, client)
                continue

            print(f"RESPOSTA:\n {message_decoded}")
        except Exception as ex:
            print("\n Não foi possível permanecer conectado no servidor!!")
            client.close()
            break

def receave_file(file_message, client):
    splited_message = file_message.split(" ")
    file_name = splited_message[1]

    file = open(file_name, 'wb+')
    while True:
        data = client.recv(4096)
        is_last_line = b"EOF" in data
        if is_last_line:
            data = data.replace(b"EOF", b"")
            file.write(data)
            break
        file.write(data)
    
    file.flush()
    file.close()
    print("Arquivo recebido com sucesso!")
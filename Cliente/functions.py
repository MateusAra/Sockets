
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

def receave_file(client_name, message, conn):
    file_name = input("Nome do arquivo: ")
    valid = file_verify(file_name, conn)
    if (valid):
        conn.send(client_name.encode())
        server_command = str.encode(f"3 {file_name}")
        conn.send(server_command)
        with open(file_name, 'wb') as file:
            while True:
                data = conn.recv(10000000)
                if b"EOF" in data:
                    break
                file.write(data)

        print("Arquivo recebido com sucesso!")
    else:
        print("Arquivo não encontrado!")
    
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
            message = str(input("OPÇÃO: "))

            if message != None:
                if int(message) > 5 or int(message) <= 0:
                    raise ValueError
                if message == "3":
                    receave_file(client_name, message, client)
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
            menu()
            messageReceive = client.recv(1024)
            print(f"RESPOSTA:\n {messageReceive.decode()}")
        except:
            print("\n Não foi possível permanecer conectado no servidor!!")
            print("Pressione <Enter> para continuar...")
            client.close()
            break


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

def receave_file(file_name, conn):
    file_name = input("Nome do arquivo: ")
    server_command = str.encode(f"3 {file_name}")
    conn.send(server_command)
    with open(file_name, 'wb') as file:
        while True:
            data = conn.recv(10000000)
            if b"EOF" in data:
                break
            file.write(data)

    print("Arquivo recebido com sucesso!")
    
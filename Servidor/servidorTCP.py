from socket import *
from server_functions import hora, list_files, send_file, send_system_data
from sys import argv
from server_utils import list_to_str

HOST  = 'localhost'
PORT  = 5000

print(f"HOST:{HOST}, PORT:{PORT}")

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

print ('Aguardando conexão de um cliente')

conn, ender = server.accept()
print ('Conectado em', ender)

while True:
   data = conn.recv(1024)
   str_data = data.decode()

   if not data:
      print ('Fechando a conexão')
      conn.close()
      break
   
   print("Recebendo dados do cliente...")
   print(f"Comando escolhido: {str_data}")

   if str_data == "1":
      print("Enviando informações...")
      system_data = send_system_data()
      conn.send(system_data.encode())

   if str_data == "2":
      print("Enviando hora atual...")
      conn.send(hora().encode())
   elif "3" in str_data:
      command_args = str_data.split(" ")[1]
      print("Enviando arquivo...")
      try:
         arquivos = list_files()
         arquivos_str = list_to_str(arquivos)

         if command_args not in arquivos_str:
            raise Exception("Arquivo não encontrado ou não existe")

         send_file(command_args, conn)
         print("Arquivo enviado com sucesso!")
      except Exception as ex:
        erro = f"Erro: {ex}"
        conn.send(erro.encode())
        
   elif str_data == "4":
      print("Enviando lista de arquivos...")
      server_files = list_files()
      server_files_str = list_to_str(server_files)
      conn.send(server_files_str.encode())

   
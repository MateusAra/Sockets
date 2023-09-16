from socket import *
from server_functions import hora, list_files
from sys import argv
from server_utils import list_to_str

HOST  = 'localhost'
PORT  = 5000

print(f"HOST:{HOST}, PORT:{PORT}")

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(3)

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
   elif str_data == "2":
      conn.send(hora().encode())
   elif str_data == "4":
      server_files = list_files()
      server_files_str = list_to_str(server_files)
      conn.send(server_files_str.encode())
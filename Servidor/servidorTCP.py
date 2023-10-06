import re
from socket import *
import sys
from server_functions import list_files, send_file, send_system_data, time_now
from sys import argv
from server_utils import list_to_str
import threading

HOST = 'localhost'
PORT = 5000

print (f'Servidor aguardando conexão de clientes\n HOST: {HOST} | PORT: {PORT}')

clients = []

def main():

   tcp_server = socket(AF_INET, SOCK_STREAM)
   
   try:
      tcp_server.bind((HOST, PORT))
      tcp_server.listen()
   except:
      return print("\n Não foi possível iniciar o servidor!\n")
   
   while True:
      client, ender = tcp_server.accept()
      clients.append(client)

      thread = threading.Thread(target=messages_treatement, args=[client])
      thread.start()

def messages_treatement(client):
    while True:
        try:
            message = client.recv(4096)
            str_data = message.decode()
            if not message:
               print ('Fechando a conexão')
               client.close()
               break
            
            print(f"\nComando recebido: {str_data}")

            match = re.search(r"Opção:\s*(\d+)", str_data)

            if match is not None:
               option = match.group(1)

            if option == "1":
               print("Enviando informações...")
               system_data = send_system_data()
               broadcast(system_data.encode(), client)

            elif option == "2":
               print("Enviando hora atual...")
               hora = time_now()
               broadcast(hora.encode(), client)
               
            elif option == "3":
               match = re.search(r"Opção:\s*(\d+)\s+(.*)", str_data)

               if match is not None:
                  file_name = match.group(2)
               print("Enviando arquivo...")
               arquivos = list_files()
               arquivos_str = list_to_str(arquivos)
               if file_name not in arquivos_str:
                  raise Exception("Arquivo não encontrado ou não existe")
               
               send_file(file_name, client)
               print("Arquivo enviado com sucesso!")
                  
            elif option == "4":
               print("Enviando lista de arquivos...")
               server_files = list_files()
               server_files_str = list_to_str(server_files)
               broadcast(server_files_str.encode(), client)
               
            else:
               broadcast("\nComando não tratado\n".encode(), client)
            
        except Exception as ex:
            erro = f"Erro: {ex}"
            broadcast(erro.encode(), client)
            #delete_client(client)
            break

def broadcast(message, client):
    for clientItem in clients:
      if clientItem == client:
         try:
            clientItem.send(message)
         except:
            delete_client(clientItem)

def delete_client(client):
   clients.remove(client)

main()
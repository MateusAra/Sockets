from socket import *
from server_functions import hora, list_files, send_file, send_system_data
from sys import argv
from server_utils import list_to_str
import threading

HOST = 'localhost'
PORT = 5000

print (f'Servidor aguardando conexão de clientes\n HOST{HOST} | PORT {PORT}')

clients = []

def main():

   server = socket(AF_INET, SOCK_STREAM)
   
   try:
      server.bind((HOST, PORT))
      server.listen()
   except:
      return print("\n Não foi possível iniciar o servidor!\n")
   
   while True:
      client, ender = server.accept()
      clients.append(client)

      thread = threading.Thread(target=messages_treatement, args=[client])
      thread.start()




def messages_treatement(client):
    while True:
        try:
            message = client.recv(2048)
            str_data = message.decode()
            if not message:
               print ('Fechando a conexão')
               client.close()
               break
            
            print(f"\nComando recebido: {str_data}")

            if str_data == "1":
               print("Enviando informações...")
               system_data = send_system_data()
               broadcast(system_data.encode(), client)

            if str_data == "2":
               print("Enviando hora atual...")
               hora = hora()
               broadcast(hora.encode(), client)

            elif "3" in str_data:
               command_args = str_data.split(" ")[1]
               print("Enviando arquivo...")
               try:
                  arquivos = list_files()
                  arquivos_str = list_to_str(arquivos)

                  if command_args not in arquivos_str:
                     raise Exception("Arquivo não encontrado ou não existe")

                  send_file(command_args, client, clients)
                  print("Arquivo enviado com sucesso!")
               except Exception as ex:
                  erro = f"Erro: {ex}"
                  broadcast(erro.encode(), client)
               
            elif str_data == "4":
               print("Enviando lista de arquivos...")
               server_files = list_files()
               server_files_str = list_to_str(server_files)
               broadcast(server_files_str.encode(), client)
            else:
               broadcast("\nComando não tratado\n".encode(), client)
            
        except:
            delete_client(client)
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
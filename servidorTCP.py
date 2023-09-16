

from socket import *

HOST  = 'localhost'
PORT  = 5000

print(f"HOST:{HOST}, PORT:{PORT}")

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen([3])

print ('Aguardando conexão de um cliente')

conn, ender = server.accept()
print ('Conectado em', ender)

while True:
   data = conn.recv(1024)
   print(data.decode())
   if not data:
      print ('Fechando a conexão')
      conn.close()
      break
   conn.send(data.decode())

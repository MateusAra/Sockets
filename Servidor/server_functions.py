from datetime import datetime
from os import listdir, path
from pathlib import Path
import platform

def time_now():
    return datetime.now().strftime("%H:%M:%S")

def list_files():
    script_dir = Path(__file__).parent.absolute()
    script_path = path.join(script_dir, "server_files")

    return listdir(str(script_path))
def send_file(file_name: str, conn, clients):
    script_dir = Path(__file__).parent.absolute()
    script_path = path.join(script_dir, "server_files", file_name)

    with open(script_path, "rb") as file:
        for data in file.readlines():
            broadcast_file(data, conn, clients)
        broadcast_file(b"EOF", conn, clients)


def send_system_data():
    system_info = "\nSistema atual: " + platform.system()
    processor_info = "\nProcessador: " + platform.processor()
    architecture_info = platform.architecture()
    architecture_info_string = "\nArquitetura: " + " ".join(architecture_info)
    python_version = "\nPython (versão): " + platform.python_version()
    pc_name = "\nNome do computador: " + platform.node()
    informacoes = system_info + processor_info + architecture_info_string + python_version + pc_name
    return informacoes


def broadcast_file(clients, message, client):
    for clientItem in clients:
      if clientItem == client:
         try:
            clientItem.send(message)
         except:
            clients.remove(clientItem)



from datetime import datetime
from os import listdir, path
from pathlib import Path

def hora():
    return datetime.now().strftime("%H:%M:%S")
def list_files():
    script_dir = Path(__file__).parent.absolute()
    script_path = path.join(script_dir, "server_files")

    return listdir(str(script_path))
def send_file(file_name: str, conn):
    script_dir = Path(__file__).parent.absolute()
    script_path = path.join(script_dir, "server_files", file_name)

    with open(script_path, "rb") as file:
        for data in file.readlines():
            conn.send(data)
        conn.send(b"EOF")
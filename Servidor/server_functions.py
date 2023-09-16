from datetime import datetime
from os import listdir, path
from pathlib import Path

def hora():
    return datetime.now().strftime("%H:%M:%S")
def list_files():
    script_dir = Path(__file__).parent.absolute()
    script_path = path.join(script_dir, "server_files")

    return listdir(str(script_path))
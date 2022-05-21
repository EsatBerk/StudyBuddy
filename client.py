import socket
import tqdm
import os
import tkinter as tk
from tkinter import filedialog
import hashlib

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


file_path= file_path.encode()

print("SHA-512:", hashlib.sha512(file_path).hexdigest())

host = "192.168.0.16"
port = 5001


filesize =  os.path.getsize(file_path)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")

s.connect((host,port))
print("[+] Connected. ")


s.send(f"{file_path}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {file_path}")
with open (file_path,"rb") as f:
        while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:

                        break

                s.sendall(bytes_read)
                progress.update(len(bytes_read))

s.close()

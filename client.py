import socket
import tqdm
import os
import tkinter as tk
from tkinter import filedialog


BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


file_path= file_path.encode()



host = "192.168.1.30"
port = 5001


filesize =  os.path.getsize(file_path)

client = socket.socket()

print(f"[+] Connecting to {host}:{port}")

client.connect((host, port))
print("[+] Connected. ")
msg = client.recv(1024)
print(msg.decode("utf-8"))


client.send(f"{file_path}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {file_path}")
with open (file_path,"rb") as f:
        while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:

                        break

                client.sendall(bytes_read)
                progress.update(len(bytes_read))

print("Successful")
client.close()

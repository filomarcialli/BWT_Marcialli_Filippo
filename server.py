# SERVER

import socket as sck

IP = "127.0.0.1"
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    server.bind((IP, PORTA))
    server.listen(5)
    print("Server avviato. In attesa di un client...")
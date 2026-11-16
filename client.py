# CLIENT

import socket as sck

IP = "127.0.0.1"
PORTA = 5000

parola = input("Inserisci la parola da inviare al server: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect((IP, PORTA))
    client.sendall(parola.encode())
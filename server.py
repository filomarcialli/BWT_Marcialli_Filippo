# SERVER

import socket as sck

IP = "127.0.0.1"
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    server.bind((IP, PORTA))
    server.listen(5)
    print("Server avviato. In attesa di un client...")

    conn, addr = server.accept()

with conn:
    print("Connessione stabilita con:", addr)

    dati = conn.recv(1024)
    parola_ricevuta = dati.decode()

    print("Parola ricevuta dal client:", parola_ricevuta)
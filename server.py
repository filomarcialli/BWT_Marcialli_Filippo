# SERVER

import socket as sck
import BWT_executor

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

    parola_ricevuta = parola_ricevuta + "$"

    rotazioni = BWT_executor.genera_rotazioni(parola_ricevuta)
    rotazioni = BWT_executor.ordina_rotazioni(rotazioni)
    risultato = BWT_executor.calcola_bwt(rotazioni)

    print("BWT calcolata:", risultato)
    conn.sendall(risultato.encode())

print("Server terminato.")
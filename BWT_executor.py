# BURROWS-WHEELER

def genera_rotazioni(parola):
    rotazioni = []
    
    for i in range(len(parola)):
        rotazioni = parola[i:] + parola[:i]
        rotazioni.appened(rotazione)

        return rotazione

parola = input("Inserisci una parola: ")
parola = parola + "$"




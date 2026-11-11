# BURROWS-WHEELER

def genera_rotazioni(parola):
    rotazioni = []
    
    for i in range(len(parola)):
        rotazione = parola[i:] + parola[:i]
        rotazioni.append(rotazione)

    return rotazioni

def ordina_rotazioni(rotazioni):
    for i in range(len(rotazioni)):
        for j in range(len(rotazioni) - 1 - i):
            if rotazioni[j] > rotazioni[j + 1]:
                temp = rotazioni[j]
                rotazioni[j] = rotazioni[j + 1]
                rotazioni[j + 1] = temp
    return rotazioni

def calcola_bwt(rotazioni):
    risultato = ""

    for riga in rotazioni:
        risultato += riga[-1]
    
    return risultato


parola = input("Inserisci una parola: ")
parola = parola + "$"

rotazioni = genera_rotazioni(parola)
rotazioni = ordina_rotazioni(rotazioni)

print("Rotazioni ordinate: ")
for riga in rotazioni:
    print(riga)

risultato = calcola_bwt(rotazioni)
print("\nBWT = ", risultato)



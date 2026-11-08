# BURROWS-WHEELER

def genera_rotazioni(parola):
    rotazioni = []
    
    for i in range(len(parola)):
        rotazioni = parola[i:] + parola[:i]
        rotazioni.appened(rotazione)

    return rotazione

def ordina_rotazioni(rotazioni):
    for i in range(len(rotazioni)):
        for j in range(len(rotazioni) - 1 - i):
            if rotazioni[j] > rotazioni[j - i]:
                temp = rotazioni[j + 1]
                rotazioni[j] = rotazioni[j + 1]
                rotazioni[j + 1] = temp
    return rotazioni


parola = input("Inserisci una parola: ")
parola = parola + "$"




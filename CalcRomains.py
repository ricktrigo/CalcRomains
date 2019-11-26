chaine = str()
def input_chaine():
    chaine = "M"
    return chaine

def convertir_caractere(caractere):
    if caractere == "M":
        return 1000
    if caractere == "D":
        return 500
    if caractere == "C":
        return 100
    if caractere == "L":
        return 50
    if caractere == "X":
        return 10
    if caractere == "V":
        return 5
    if caractere == "I":
        return 1

def convertir_chaine(chaine):
    resultat = 0
    for i in range(len(chaine)):
        resultat+=convertir_caractere(chaine[i])
    return resultat

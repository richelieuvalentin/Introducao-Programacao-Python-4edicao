# Escreva uma função que recebe dois números e retorne True se o primeiro for múltiplo do segundo

def multiplo (a, b):
    if a % b == 0:
        return True
    else:
        return False

multiplo(8, 4)
multiplo(7, 3)
multiplo(5, 5)

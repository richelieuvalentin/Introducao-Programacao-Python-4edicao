# Calcula a media de um lista

def media (lista):
    total = 0
    for i in lista:
        total += i
    return total / len(lista)

lista = [15, 25, 10, 5, 10, 5, 10, 5, 10, 5]

media(lista)
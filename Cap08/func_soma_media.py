# Media de Valores de uma lista

def soma(lista):
    total = 0
    for x in lista:
        total = total + x
    return total

def media(lista):
    return soma(lista) / len(lista)

lista = [10, 20, 10, 20]

media(lista)
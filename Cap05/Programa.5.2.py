# Programa 5.2: Imprime apenas os números pares entre 0 e o número digitado

fim = int(input("Digite o último número a imprimmir: "))
x = 0

while x <= fim:
    if x % 2 == 0:
        print(x)

    x = x + 1



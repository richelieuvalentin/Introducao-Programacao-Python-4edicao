# Programa 5.6: Calcula a soma de 10 números

n = 1
soma = 0

while n <= 10:
    x = int(input(f"Digite o {n} número: "))
    soma = soma + x
    n = n + 1

print(f"Soma: {soma}")
# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
# em vez de começar com 1 e 10.

n = int(input("Tabuada de : "))
inicio = int(input("Digite o número de início da tabuada: "))
fim = int(input("Digite o número para o fim da tabuada: "))

while inicio <= fim:
    print(n, "X", inicio, "=", n * inicio)
    inicio = inicio + 1
    
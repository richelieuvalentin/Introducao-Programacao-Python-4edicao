# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo
#segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
#podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

# recebe dois números a e b
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# inicializa duas variaveis
# Um contador começando em 1 e acumulador(resultado) começando em 0
resultado = 0
contador = 1

# Enquanto o contador for menor ou igual a b
# Adiciona "a" ao resultado 
while contador <= b:
    resultado = resultado + a
    contador = contador + 1

print(a, "x", b, "=", resultado)

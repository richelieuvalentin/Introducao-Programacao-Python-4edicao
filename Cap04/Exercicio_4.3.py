# Escreva um programa que leia três números e que imprima o maior e o menor.

Num_1 = float(input("Digite o primeiro número: "))
Num_2 = float(input("Digite o segundo número: "))
Num_3 = float(input("Digite o terceiro número: "))

if Num_1 > Num_2 and Num_2 > Num_3:
    maior = Num_1
    menor = Num_3

if Num_1 > Num_3 and Num_3 > Num_2:
    maior = Num_1
    menor = Num_2

if Num_2 > Num_1 and Num_1 > Num_3:
    maior = Num_2
    menor = Num_3

if Num_2 > Num_1 and Num_1 < Num_3:
    maior = Num_2
    menor = Num_1

if Num_3 > Num_1 and Num_1 > Num_2:
    maior = Num_3 
    menor = Num_2

if Num_3 > Num_2 and Num_2 > Num_1:
    maior = Num_3 
    menor = Num_1

print("O maior é: ", maior, "O menor número é: ", menor)
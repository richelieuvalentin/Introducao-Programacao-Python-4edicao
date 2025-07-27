# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número:"))

operação = input("Qual operação vocÊ deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/)?")


if operação == "+":
    soma = num1 + num2
    print("O resultado da soma é:", soma)

elif operação == "-":
    subtração = num1 - num2
    print("O resultado da subtração é:", subtração)

elif operação == "/" and num2 != 0:
    divisão = num1 / num2
    print("O resultado da divisão é:", divisão)

elif operação == "/" and num2 == 0:

    print("###ERRO: divisão por zero não definida!###")

elif operação == "*":
    multiplicação = num1 * num2
    print("O resultado da multiplicação é:", multiplicação)

else:
    print("Opção inválida!!!")


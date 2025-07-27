# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para
# comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

#+---------------------------------------+
#|   Preço por tipo e faixa de consumo   |
#+---------------------------------------+
#| Tipo        | Faixa (kWh)   | Preço   |
#+=======================================+
#| Residencial | Até 500       | R$ 0,40 |
#|             | Acima de 500  | R$ 0,65 |
#+---------------------------------------+
#| Comercial   | Até 1000      | R$ 0,55 |
#|             | Acima de 1000 | R$ 0,60 |
#+---------------------------------------+
#| Industrial  | Até 5000      | R$ 0,55 |
#|             | Acima de 5000 | R$ 0,60 |
#+---------------------------------------+

quantidade_kwh = float(input("Digite a quantidade de Kwh consumida: "))
tp_instalçao = input("Qual o tipo de instalação? R para residências, I para indústrias e C para comércios: ")

if tp_instalçao == "R":

    if quantidade_kwh < 500:
        preço = 0.40
    else:
        preço = 0.65

elif tp_instalçao == "I":

    if quantidade_kwh < 5000:
        preço = 0.55
    else:
        preço = 0.60

elif tp_instalçao == "C":

    if quantidade_kwh < 1000:
        preço =  0.55
    else:
        preço = 0.60

else:
    preço = 0
    print("Erro: Tipo ou valor inválido!!!")

print("O preço total a pagar é :R$", round(preço * quantidade_kwh, 2))

# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

depósito = float(input("Qual o valor do depósito: "))
taxa_juro = float(input("Qual taxa a taxa de juros: "))
mes = 1
total = 0

while mes <= 24:
    total = total + depósito * taxa_juro
    print(f"Mês {mes} Valor: R$ {round(total, 2)}")
    mes = mes + 1

print(f"Total : R$ {round(total, 2)}")


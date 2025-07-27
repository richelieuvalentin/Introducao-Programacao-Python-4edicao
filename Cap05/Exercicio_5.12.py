# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será
# depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

taxa_juros = float(input("Qual a taxa de juros? "))
valorAcumulado = 0
mes = 1

while mes <= 24:
    deposito = float(input("Qual o valor do depósito deste mês? "))
    valorAcumulado = valorAcumulado + deposito * taxa_juros
    print(f"Mês {mes} Valor: R$ {round(valorAcumulado, 2)}")
    mes = mes + 1

print(f"Total: R$ {round(valorAcumulado, 2)}")
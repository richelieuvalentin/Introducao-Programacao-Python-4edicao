# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salário = float(input(" Digite o valor do salário: "))
percentual_aumento = 0


if salário <= 1250:
    percentual_aumento = 0.15
    novo_salário = salário + (salário * percentual_aumento)
  

if salário > 1250:
    percentual_aumento = 0.10
    novo_salário = salário + (salário * percentual_aumento)

print("O novo salário é :R$", salário, " o aumento foi de ", percentual_aumento *100, "%", "ou seja de R$", salário * percentual_aumento)
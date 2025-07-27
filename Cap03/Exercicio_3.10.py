# Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

salário = float(input('Digite o valor do seu salário: '))
percentual_aumento = float(input('Digite o percentual do aumento: '))

aumento = salário * (percentual_aumento/100)
novo_salário = salário + aumento

print('O valor do aumento é R$', aumento)
print('O novo salário será de R$', novo_salário)


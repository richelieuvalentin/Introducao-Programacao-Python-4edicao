# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.

preço_mercadoria = float(input('Digite o preço da mercadoria: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

desconto = preço_mercadoria * (percentual_desconto/100)
preço_a_pagar = preço_mercadoria - desconto

print('O valor do desconto foi de R$', desconto)
print('O preço a pagar será de R$', preço_a_pagar)

end = input(" ")


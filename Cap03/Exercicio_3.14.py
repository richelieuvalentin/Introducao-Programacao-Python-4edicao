# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km_rodados = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

custo_km_rodado = 0.15
diaria_carro = 60

preço_a_pagar = (km_rodados * custo_km_rodado) + (diaria_carro * diaria_carro)

print('O preço a pagar foi de R$ ', preço_a_pagar)
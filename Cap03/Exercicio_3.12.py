# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Qual a distância a percorrer? '))
velocidade_media = float(input('Qual a será a velocidade média esperada para a viagem? '))

tempo_viagem = distancia / velocidade_media

print('O tempo da viagem será de ', tempo_viagem, 'horas.')
# Escreva um programa que converta uma temperatura digitada em °C em °F

temp_celsius = float(input('Digite uma temperatura em graus Celsius: '))

# F = 9 x C / 5 +32 

temp_farenheit = ((9 * temp_celsius) / 5) + 32

print('A temperatura em Farenheit é ', temp_farenheit)
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidad de cigarros fumados por dia e quantos anos ele já fumou
# Considere que um fumante perde 10 minutos de vida a cada cigarro
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias

cigarros_dia = int(input('Digite quantos cigarros por dia: '))
anos_fumante = int(input('Digite quantos anos fumou: '))

dias_fumante = anos_fumante * 365
minutos_cigarro = 10
tempo_perdido_minutos = dias_fumante * minutos_cigarro * cigarros_dia

dias_perdidos = tempo_perdido_minutos / 1440

print('Dias perdidos : ', dias_perdidos)
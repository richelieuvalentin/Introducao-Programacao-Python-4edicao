# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago. 
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input("Qual o valor da dívida? "))
juro_mensal = float(input("Qual a taxa de juros? "))
pag_mensal = float(input("Qual o valor de pagamento mensal? "))

saldo_devedor = divida
meses = 1
total_pago = 0

while saldo_devedor > 0:
    saldo_devedor = saldo_devedor * juro_mensal - pag_mensal
    total_pago = total_pago + pag_mensal * meses
    meses = meses + 1

juros_pago = total_pago - divida
    
print(f"A dívida será paga em {meses} meses. O total pago foi R$ {round(total_pago, 2)}, o total de juros foi R$ {round(juros_pago, 2)}")

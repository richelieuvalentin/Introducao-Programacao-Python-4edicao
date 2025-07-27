# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_imovel = float(input("Qual o valor da casa? "))
salário = float(input("Digite o valor do seu salário: "))
prazo = int(input("Digite o prazo em anos que deseja pagar o financiamento: "))

prestação = valor_imovel / (prazo * 12)

if prestação < salário * 0.3:
    print("Empréstrimo aprovado!")
    print("Valor do imóvel:", valor_imovel)
    print("Prazo:", prazo * 2, "meses. Prestação:R$",round(prestação, 2))

else:
    print("Empréstimo reprovado!")


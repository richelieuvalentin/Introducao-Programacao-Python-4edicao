# Programa 4.9: Categoria x preço, usando elif

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preço = 10

elif categoria == 2:
    preço = 18

elif categoria == 3:
    preço = 23

elif categoria == 4:
    preço = 26

elif categoria == 5:
    preço = 31

else:
    print("Categoria inválida, digite um valor entre 1  e 5!")

print("O preço do produto é : R$", preço)


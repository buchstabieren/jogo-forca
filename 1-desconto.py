print("Boas vindas a Loja da Buchstabieren Hermes!")

valorUnitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

valorTotalSemDesconto = valorUnitario * quantidade

if valorTotalSemDesconto < 2500:
    desconto = 0
elif valorTotalSemDesconto >= 2500 and valorTotalSemDesconto < 6000:
    desconto = 0.04
elif valorTotalSemDesconto >= 6000 and valorTotalSemDesconto < 10000:
    desconto = 0.07
elif valorTotalSemDesconto >= 10000:
    desconto = 0.11
else:
    print("Valor inválido!")

valorComDesconto = valorTotalSemDesconto - (valorTotalSemDesconto * desconto)

print(f"Valor total sem desconto: R$ {valorTotalSemDesconto:.2f}")
print(f"Valor total com desconto: R$ {valorComDesconto:.2f}")
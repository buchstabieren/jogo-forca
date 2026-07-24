print("Bem-vindo à Loja de Açaí e Cupuaçu da Buchstabieren Hermes!\n")

#usando formatação de strings (f-string) para deixar tudo alinhado

print("-" * 55)
print(f'{"Cardápio":^55}')
print("-" * 55)
print(f'| {"Tamanho":^10} | {"Cupuaçu (CP)":^15} | {"Açaí (AC)":^15} |')
print("-" * 55)
print(f'| {"P":^10} | {"R$ 9.00":^15} | {"R$ 11.00":^15} |')
print(f'| {"M":^10} | {"R$ 14.00":^15} | {"R$ 16.00":^15} |')
print(f'| {"G":^10} | {"R$ 18.00":^15} | {"R$ 20.00":^15} |')
print("-" * 55)

#^10 → centraliza o texto em 10 caracteres.
#^15 → centraliza em 15 caracteres.
#- * 55 → cria uma linha com 55 hífens.

acumulador = 0

while True:

    while True:
        sabor = input("Digite o sabor do produto (CP/AC): ") #colocar . maiusculas todas as letras 
        
        if sabor == "CP" or sabor == "AC":
            break

        print("Sabor inválido. Tente novamente CP para Cupuaçu e AC para Açaí\n")

    while True:
        tamanho = input("Digite o tamanho do produto (P/M/G): ")
        
        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            break

        print("Tamanho inválido. Tente novamente P para pequeno, M para médio e G para grande\n")
    

    print(f"Sabor {sabor} | Tamanho {tamanho}")

    match(sabor):
        case "CP":
            match(tamanho):
                case "P":
                    valor = 9
                case "M":
                    valor = 14
                case "G":
                    valor = 18
        case "AC":
            match(tamanho):
                case "P":
                    valor = 11
                case "M":
                    valor = 16
                case "G":
                    valor = 20

    acumulador += valor

    print(f"Com valor de {valor}\n")

    comprarMais = input("Deseja pedir mais alguma coisa? (S/N): ")

    match(comprarMais):
        case "S":
            continue
        case "N":
            print(f"Valor total do pedido: R$ {acumulador:.2f}")
            break
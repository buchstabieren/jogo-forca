import fileHandler as fH
import jogo as j

def mostrarMenu():
    print("\n\n================================")
    print("Bem-vindo ao jogo da forca!")
    print("================================\n")
    print("Escolha uma opção:")
    print("1 - Jogar")
    print("2 - Score")
    print("3 - Sair\n")

arquivo = 'score.txt'

if fH.existeArquivo(arquivo):
    print("Arquivo localizado no pc!")
else: 
    print("Arquivo não existe")
    fH.criarArquivo(arquivo)

# while opcao != 3:
while True:
    mostrarMenu()
    opcao = int(input('Digite uma opção (1/2/3): '))

    match(opcao):
        case 1:
            print("Iniciando jogo...\n")
            j.jogar()

        case 2:
            print("SCORE DO JOGO...\n")
            dados = fH.listarArquivo(arquivo)
            if not dados:
                print("Score vazio")
            else:
                i = 1
                for jogador in dados:
                    print(f'{i} -> {jogador}')
                    i += 1

        case 3:
            print("Saindo do jogo...\n") 
            break

        case _:
            print("Opção inválida. Tente outra opção!\n")

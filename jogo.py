import fileHandler as fH
from random import choice
import desenhos as d

def jogar(): #aqui eu carrego toda a lista de palavras do arquivo para a lista de palavras do jogo, e depois sortear uma palavra aleatória para o jogador adivinhar 
    listaPalavras = []
    arquivo = fH.abrirArquivoLeitura('palavras.txt')

    for linha in arquivo:
        palavra = linha.strip()
        listaPalavras.append(palavra)

    palavraSorteada = choice(listaPalavras)

    for space in range(10):
        print() # só para dar espaço no terminal

    digitadas = []
    acertos = []
    erros = 0

    jogador = input("Quem está jogando? Digite seu nome: ")

    while True: #aqui eu começo as verificações do jogo, se o jogador acertou a palavra secreta ou se errou, e também vai exibir a forca de acordo com os erros do jogador
        adivinha = d.imprimirPalavraSecreta(palavraSorteada, acertos)

        #CONDIÇÃO DE VITÓRIA
        if adivinha == palavraSorteada:
            print(f'Parabéns {jogador}! Você acertou a palavra secreta: {adivinha}')
            score = d.desenharForca(erros)
            fH.inserirScore('score.txt', jogador, score)
            break

        #TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip() #para não ter problemas com letra maiuscula ou espaços em branco

        if tentativa in digitadas: #se a tentativa estiver na lista de digitadas, ele vai avisar que já tentou e vai continuar o loop
            print(f'Você já tentou a letra "{tentativa}". Tente outra letra.')
            continue #volta para o início do loop
        else:
            digitadas += tentativa #ou append() também funciona

            if tentativa in palavraSorteada: #se existe a letra na palavra sorteada, ele vai adicionar a letra na lista de acertos para exibir letras que estão presentes na palavra sorteada
                acertos += tentativa 
            else:
                erros += 1
                print(f"Ops! Você errou! A letra '{tentativa}' não está na palavra secreta.")

        score = d.desenharForca(erros)

        #CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
                print("\nENFORCADO!!!")
                print(f'A palavra secreta era: {palavraSorteada}')
                break

    fH.inserirScore('score.txt', jogador, score)
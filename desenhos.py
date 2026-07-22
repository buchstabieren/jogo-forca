def imprimirPalavraSecreta(palavra, acertos):
    adivinha = ''

    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '\u2588' # Unicode para o bloco sólido é '\u2588', um quadrado sólido que representa uma letra oculta, preenchido preto

    print(f'Adivinhe a palavra que tem ({len(palavra)} letras): ')
    for letra in adivinha:
        print(f'{letra} ', end='')
    print() 

    return adivinha

def desenharForca(erros):
    score = 1000

    print('|__.__')
    print("|  :  ")

    if erros >= 1:
        print("|  O  ")
        score = 800
    else:
        print("|")

    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
        score = 600
    elif erros == 3:
        linha2 = " /|  "
        score = 400
    elif erros >= 4:
        linha2 = " /|\ "
        score = 200
    print(f'|{linha2}')

    linha3 = ""
    if erros == 5:
        linha3 += " /   "
        score = 100
    elif erros >= 6:
        linha3 += " / \ "
        score = 0

    print(f"|{linha3}")

    print(f"|\n_________")

    return score
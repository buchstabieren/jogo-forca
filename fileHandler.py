# manipulador de arquivos

def existeArquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo, 'rt') # r = read, t = text
        arq.close()
        return True
    except FileNotFoundError:
        return False

def abrirArquivoLeitura(nomeArquivo):
    try:
        arq = open(nomeArquivo, 'r') # r = read
        print(f'Arquivo {nomeArquivo} aberto com sucesso!\n')
        return arq
    except:
        print('Não foi possível abrir o arquivo para leitura!')
        return None

def criarArquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo, 'wt+') # w = write, t = text, + = create if not exists
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo!')

def listarArquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo, 'rt')

        #print(f'Lista de palavras do arquivo {nomeArquivo}:\n')

        #for linha in arq:
            #dado = linha.strip()
            #print(f'  {dado}')

        dados = arq.readlines() 

    except:
        print('Não foi possível ler o arquivo!')

    finally:
        arq.close()
        return dados

def escreverArquivo(nomeArquivo, texto):
    try:
        arq = open(nomeArquivo, 'at') # a = append(append é acrescentar), t = text 
        arq.write(texto + '\n')
        arq.close()
        print(f'Texto adicionado ao arquivo {nomeArquivo} com sucesso!\n')
    except:
        print('Não foi possível escrever no arquivo!')

def inserirScore(nomeArquivo, nome, score):
    try:
        arq = open(nomeArquivo, 'at') # a = append, t = text
        arq.write(f'{nome} - {score}\n')
        arq.close()
        print(f'\nScore de {nome} adicionado ao arquivo {nomeArquivo} com sucesso!\n')
    except:
        print('Não foi possível escrever no arquivo!')


# CRUD simples

def createArq(nomeArq):
    try:
        arq = open(nomeArq, 'wt+')
        print(f'Arquivo {nomeArq} criado com sucesso!\n')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo')

def readArq(nomeArq):
    try:
        arq = open(nomeArq, 'rt')
        print(f'Arquivo {nomeArq} aberto para leitura')
        arq.close()
    except:
        print(f'Não foi possível abrir o arquivo {nomeArq} para leitura!')
        arq.close()

def updateArq(nomeArq, text):
    try:
        arq = open(nomeArq, 'at')
        arq.write(text + '\n')
        arq.close()
    except:
        print(f'Não foi possível escrever no arquivo {nomeArq}!')
        arq.close()

def deleteArq(nomeArq):
    try:
        arq = open(nomeArq, 'wt')
        arq.close()
        print(f'Arquivo {nomeArq} apagado com sucesso!\n')
    except:
        print(f'Não foi possível apagar o arquivo {nomeArq}!')
        arq.close()

# aqui ele apaga o que estava escrito dentro do arquivo, mas não apaga o arquivo em si. Ele cria um novo arquivo vazio com o mesmo nome
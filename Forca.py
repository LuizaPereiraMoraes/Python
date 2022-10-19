import random

#ADICIONAR UMA PALAVRA E A SUA DICA
def adicionar_palavra():
    while True:
        palavras = input("Digite sua nova palavra: ")
        with open('palavras.txt', 'a', encoding="utf8") as arquivo:
            arquivo.write(palavras +'\n')

        dicas = input("Digite a dica da sua palavra: ")
        with open('dicas.txt', 'a', encoding="utf8") as dica:
            dica.write(dicas +'\n')

        resposta = input("Você deseja adicionar mais uma palavra[S]/[N]? ").upper()
        if resposta == 'S':
            return adicionar_palavra()
        else:
            return jogar()

#EXCLUIR UMA PALAVRA
def excluir_palavra():
    palavras = open('palavras.txt', 'r', encoding="utf8").read().split('\n')
    dicas = open('dicas.txt', 'r',encoding="utf8").read().split('\n')
    palavras.pop()
    dicas.pop()
    excluir = input("Digite a palavra que deseja excluir: ")
    for indice, palavra in enumerate(palavras):
        if palavra == excluir:
            palavras.remove(palavra)
            dicas.pop(indice)
        else:
            print("Essa palavra não está na sua lista!")
            return excluir_palavra()
    with open('palavras.txt', 'w', encoding="utf8") as arquivo:
        for valor in palavras:
            arquivo.write(valor + '\n')
    with open('dicas.txt', 'w', encoding="utf8") as arquivo_dicas:
        for valor in dicas:
            arquivo_dicas.write(valor + '\n')

    resposta = input("Você deseja adicionar mais uma palavra[S]/[N]? ").upper()
    if resposta == 'S':
        return excluir_palavra()
    else:
        return jogar()

#PEGAR A PALAVRA ALEATÓRIA
def aleatorio():
    arquivo = open('palavras.txt', 'r', encoding="utf8").read().split("\n")
    dicas = open('dicas.txt', 'r', encoding="utf8").read().split("\n")
    numero_aleatorio = random.randint(0, len(arquivo) - 1)
    dica = dicas[numero_aleatorio]
    palavra_secreta = arquivo[numero_aleatorio]
    print("A sua palavra: ", dica)
    return palavra_secreta

#DESENHO DA FORCA
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#INÍCIO DO JOGO
def jogar():
    print("Bem vindo(a) ao jogo da forca. Lembre-se você tem 7 tentativas!")
    palavra_secreta = aleatorio()
    erros = 0
    lista_incognita = []
    lista_erros = []
    for pos in range(len(palavra_secreta)):
        lista_incognita.append('_')
    while erros != 7:

        palavra = ''.join(lista_incognita)
        if palavra == palavra_secreta:
            print(palavra_secreta)
            print("VOCÊ ACERTOU!!")
            break

        print(*lista_incognita)
        chute = input("\nDigite uma letra:  ").lower().strip()

        for pos in range(len(palavra_secreta)):
            if chute == palavra_secreta[pos]:
                lista_incognita[pos] = chute


        if chute not in palavra_secreta:
            erros += 1
            print('Ainda falta acertar algumas letras')
            print('Você ainda tem {} tentativas'.format(7 - erros))
            desenha_forca(erros)
            lista_erros.append(chute)
            print(lista_erros)
        if erros == 7:
            print('A sua palavra era: ', palavra_secreta)
            print("FIM DO JOGO!")
            break

#MENU DE OPÇÕES
if __name__ == '__main__':
    escolha = int(input('[1]Adicionar palavra\n[2]Excluir uma palavra\n[3]Jogar\nEscolha uma das opções: '))
    if escolha == 1:
        adicionar_palavra()
    elif escolha == 2:
        excluir_palavra()
    elif escolha == 3:
        jogar()

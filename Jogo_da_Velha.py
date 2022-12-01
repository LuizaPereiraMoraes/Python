import sys


def desenharJogoDaVelha():
    print(f" {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print("---|---|---")
    print(f" {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print("---|---|---")
    print(f" {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")

def jogar():
    desenharJogoDaVelha()
    jogadas = 0
    ext = False
    while jogadas != 9:
        while True:
            jogador1 = 'X'
            escolha_jogador1 = int(input("\nJogador 1(X) escolha uma posição: "))
            if escolha_jogador1 in lista_Aux:
                print("Jogada Indisponível!")
            else:
                for linha in range(0, 3):
                    if escolha_jogador1 in velha[linha]:
                        posicao = velha[linha].index(escolha_jogador1)
                        lista_Aux.append(velha[linha][posicao])
                        velha[linha][posicao] = jogador1
                        jogadas += 1
            desenharJogoDaVelha()
            if verificacao():
                print("Jogador 1(X) ganhou!")
                ext = True
                break
            if jogadas == 9:
                print("Empate! DEU VELHA")
                ext = True
                break
            break

        if ext == True:
            break



        while True:
            jogador2 = 'O'
            escolha_jogador2 = int(input("\nJogador 2(O) escolha uma posição: "))
            if escolha_jogador2 in lista_Aux:
                print("Jogada Indisponível!")

            else:
                for linha in range(0, 3):
                    if escolha_jogador2 in velha[linha]:
                        posicao = velha[linha].index(escolha_jogador2)
                        lista_Aux.append(velha[linha][posicao])
                        velha[linha][posicao] = jogador2
                        jogadas += 1
            desenharJogoDaVelha()
            if verificacao():
                print("Jogador 2(O) ganhou!")
                ext = True
                break
            break

        if ext == True:
            break



def verificacao():
    # Vitória em linha
    if ("X" == velha[0][0] and "X" == velha[0][1] and "X" == velha[0][2]) or ("X" == velha[1][0] and "X" == velha[1][1] and "X" == velha[1][2]) or ("X" == velha[2][0] and "X" == velha[2][1] and "X" == velha[2][2]):
        return True
    elif ("O" == velha[0][0] and "O" == velha[0][1] and "O" == velha[0][2]) or ("O" == velha[1][0] and "O" == velha[1][1] and "O" == velha[1][2]) or ("O" == velha[2][0] and "O" == velha[2][1] and "O" == velha[2][2]):
        return True

    # Vitória em coluna
    elif ("X" == velha[0][0] and "X" == velha[1][0] and "X" == velha[2][0]) or ("X" == velha[0][1] and "X" == velha[1][1] and "X" == velha[2][1]) or ("X" == velha[0][2] and "X" == velha[1][2] and "X" == velha[2][2]):
        return True
    elif ("O" == velha[0][0] and "O" == velha[1][0] and "O" == velha[2][0]) or ("O" == velha[0][1] and "O" == velha[1][1] and "O" == velha[2][1]) or ("O" == velha[0][2] and "O" == velha[1][2] and "O" == velha[2][2]):
        return True

    # Vitória em diagonal
    elif ("X" == velha[0][0] and "X" == velha[1][1] and "X" == velha[2][2]) or ("X" == velha[0][2] and "X" == velha[1][1] and "X" == velha[2][0]):
        return True
    elif ("O" == velha[0][0] and "O" == velha[1][1] and "O" == velha[2][2]) or ("O" == velha[0][2] and "O" == velha[1][1] and "O" == velha[2][0]):
        return True
    else:
        return False


if __name__ == '__main__':
    velha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lista_Aux = []
    escolha = int(input('[1]Jogar\n[2]Sair\nEscolha uma das opções: '))
    if escolha == 1:
        jogar()
    elif escolha == 2:
        print("Tchau...")


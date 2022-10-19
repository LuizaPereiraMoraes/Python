import random

def score(vida, chute, aleatorio):
    if aleatorio < chute:
        life = chute - aleatorio
        vida_atual = vida - life
    else:
        life = aleatorio - chute
        vida_atual = vida - life
    return vida_atual

def jogo():
    aleaorio = random.randrange(0, 100)
    vida = 50
    for chute in range(0, 3):
        chute = int(input("Digite um número entre 0 e 100: "))
        if chute > aleaorio:
            heart = score(vida, chute, aleaorio)
            vida = heart
            if vida < 0:
                print("Suas vidas acabaram. Você perdeu! O número sorteado era: ", aleaorio)
                break
            print("Você errou! O número sorteado é menor que: ", chute, "\nA sua vida está em: ", heart)
        elif chute < aleaorio:
            heart = score(vida, chute, aleaorio)
            vida = heart
            if vida < 0:
                print("Suas vidas acabaram. Você perdeu! O número sorteado era: ", aleaorio)
                break
            print("Você errou! O número sorteado é maior que: ", chute, "\nA sua vida está em: ", heart)
        else:
            print("Você acertou! O número sorteado era: ", chute)
            break

if __name__ == '__main__':
    jogo()


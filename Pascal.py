def pascal():
    base_final = int(input("Digite o número de linhas para o seu triângulo de Pascal: "))
    lista_auxiliar = []
    lista_atual = []

    for base_atual in range(0, base_final):
        for pos in range(0, base_atual + 1):
            if pos == 0 or pos == base_atual:
                lista_atual.append(1)
            else:
                lista_atual.append(lista_auxiliar[pos] + lista_auxiliar[pos-1])
        lista_auxiliar = lista_atual[:]
        print(*lista_atual)
        lista_atual.clear()


if __name__ == '__main__':
      pascal()
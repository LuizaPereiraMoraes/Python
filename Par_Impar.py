def numero_primo():
    lista = []
    numero = int(input("Digite um número: "))

    for contador in range(1, numero + 1):
        if numero % contador == 0:
             lista.append(contador)


    if len(lista) == 2:
        print(f"O seu número é primo, pois é divisível por {lista}")
    else:
        print(f"O seu número não é primo, pois é divisível por {lista}")


if __name__ == '__main__':
    numero_primo()

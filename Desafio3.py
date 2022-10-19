def triangulo():
    numero = int(input("Digite um número: "))

    for pos in range(1, numero + 1):
        print(" * " * pos)


if __name__ == '__main__':
    triangulo()

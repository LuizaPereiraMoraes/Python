def quadrado():
    numero = int(input("Digite um número: "))

    lado = numero
    while lado > 0:
        print(" * " * numero)
        lado -= 1

if __name__ == '__main__':
    quadrado()

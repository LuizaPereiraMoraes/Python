def quadrado_vazio():
    numero = int(input("Digite um número: "))

    print(" *" * numero)
    for pos in range(1, numero - 1):
        print(" *" + "  " * (numero - 2) + " *")
    print(" *" * numero)



if __name__ == '__main__':
    quadrado_vazio()

def decimal():
    decimal = int(input("Digite um número decimal para converter para o binário: "))
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = decimal % 2
        lista.insert(0, resto)
        quociente = decimal // 2
        decimal = quociente

    binario = ''.join([str(item) for item in lista])
    print("O número decimal digitado equivale em binário: ", binario)


if __name__ == '__main__':
    decimal()
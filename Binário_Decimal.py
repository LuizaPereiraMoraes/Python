def binario():
    binario = int(input("Digite um número binário para converter para o decimal: "))
    numero = len(str(binario))

    decimal = 0
    i = 0

    while numero >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        numero = numero - 1
        i = i + 1
        binario = binario // 10
    print("O número binário digitado equivale em decimal: ", decimal)


if __name__ == '__main__':
    binario()
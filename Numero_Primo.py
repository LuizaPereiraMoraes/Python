def numero_primo_while():
    lista = []
    contador = 1
    numero = int(input("Digite um número: "))

    while contador != numero + 1:
         if numero % contador == 0:
            lista.append(contador)
            contador += 1
         else:
            contador += 1


    if len(lista) == 2:
        print(f"O seu número é primo, pois é divisível por {lista}")
    else:
        print(f"O seu número não é primo, pois é divisível por {lista}")


if __name__ == '__main__':
    numero_primo_while()

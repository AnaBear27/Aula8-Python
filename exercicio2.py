def acessar_elemento_lista():
    lista_numeros = [10, 20, 30, 40, 50]

    try:
        indice = int(input(f"Digite um índice (de 0 a {len(lista_numeros) - 1}): "))

        elemento = lista_numeros[indice]
        print(f"O elemento na posição {indice} é: {elemento}")
    except IndexError:
        print("Error índice inválido. O índice deve estar dentro dos limites da lista.")

acessar_elemento_lista()
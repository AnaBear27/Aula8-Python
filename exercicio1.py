def realizar_divisao():
    try:
        numerador = int(input("Digite o numerador (número a ser dividido): "))
        denominador = int(input("Digite o denominador (número pelo qual será dividido): "))

        resultado = numerador / denominador 

        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

realizar_divisao()
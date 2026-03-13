def executar():

    while True:

        # Pedindo o primeiro número
        num1 = input("Digite o primeiro número: ")

        # Verificando se é um número
        try:
            num1 = float(num1)
        except:
            print("Erro: você precisa digitar um número válido.\n")
            continue


        # Pedindo o segundo número
        num2 = input("Digite o segundo número: ")

        # Verificando se é um número
        try:
            num2 = float(num2)
        except:
            print("Erro: você precisa digitar um número válido.\n")
            continue


        # Pedindo o operador
        operador = input("Digite a operação (+, -, *, /): ")

        # Verificando se é um operador válido
        if operador not in ["+", "-", "*", "/"]:
            print("Erro: operador inválido.\n")
            continue


        # Evitar divisão por zero
        if operador == "/" and num2 == 0:
            print("Erro: não é possível dividir por zero.\n")
            continue


        # Realizando cálculo
        if operador == "+":
            resultado = num1 + num2

        elif operador == "-":
            resultado = num1 - num2

        elif operador == "*":
            resultado = num1 * num2

        elif operador == "/":
            resultado = num1 / num2


        # Mostrando resultado
        print("\nResultado:", num1, operador, num2, "=", resultado)

        break
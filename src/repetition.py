def executar():

    while True:
        # Pedindo a palavra
        palavra = input("Digite uma palavra: ")

        # Pedindo o número de repetições
        repeticoes = input("Digite quantas vezes deseja repetir a palavra: ")

        # Verifica se é número
        if not repeticoes.isdigit():
            print("Erro: você precisa digitar um número.\n")
            continue

        repeticoes = int(repeticoes)

        # Verifica se está entre 1 e 10
        if repeticoes <= 0:
            print("Erro: o número deve ser maior que 0.\n")
            continue
        elif repeticoes > 10:
            print("Erro: o número máximo permitido é 10.\n")
            continue

        # Se passou em todas as verificações
        break


    # Mostrando o resultado
    print("\nVocê escreveu a palavra:", palavra)
    print("Você quis que ela fosse repetida", repeticoes, "vezes")
    print("Aqui estão as repetições:\n")

    # Repetindo a palavra
    for i in range(repeticoes):
        print(palavra)
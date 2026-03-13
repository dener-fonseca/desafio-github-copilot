def executar():

    while True:

        # Pedindo o nome
        nome = input("Digite seu nome: ").strip()

        # Verificando se o nome está vazio
        if nome == "":
            print("Erro: o nome não pode ficar vazio.\n")
            continue

        # Verificando se o nome contém apenas letras
        if not nome.isalpha():
            print("Erro: o nome deve conter apenas letras.\n")
            continue


        # Pedindo o sobrenome
        sobrenome = input("Digite seu sobrenome: ").strip()

        # Verificando se o sobrenome está vazio
        if sobrenome == "":
            print("Erro: o sobrenome não pode ficar vazio.\n")
            continue

        # Verificando se o sobrenome contém apenas letras
        if not sobrenome.isalpha():
            print("Erro: o sobrenome deve conter apenas letras.\n")
            continue


        # Concatenando nome e sobrenome
        nome_completo = nome + " " + sobrenome

        # Exibindo o nome completo
        print("\nSeu nome completo é:", nome_completo)

        break
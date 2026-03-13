from src import concatenation
from src import repetition
from src import calculation


while True:

    print("\nEscolha uma opção:")
    print("1 - Concatenar nome")
    print("2 - Repetir palavra")
    print("3 - Calculadora")
    print("0 - Sair")

    escolha = input("Digite a opção: ")

    if escolha == "1":
        concatenation.executar()

    elif escolha == "2":
        repetition.executar()

    elif escolha == "3":
        calculation.executar()

    elif escolha == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida")
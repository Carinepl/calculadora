def soma(x, y):
    return x + y


def subtrai(x, y):
    return x - y


def multiplica(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y


def calcula():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite a escolha (1/2/3/4): ")

        if escolha in ["1", "2", "3", "4"]:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if escolha == "1":

                print(f"{numero1} + {numero2} = {soma(numero1, numero2)}")

            elif escolha == "2":
                print(f"{numero1} - {numero2} = {subtrai(numero1, numero2)}")

            elif escolha == "3":
                print(f"{numero1} * {numero2} = {multiplica(numero1, numero2)}")

            elif escolha == "4":
                print(f"{numero1} / {numero2} = {divide(numero1, numero2)}")

            next_calculation = input("Deseja fazer outra operação? (sim/não): ")
            if next_calculation.lower() != "sim":
                break
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    calcula()

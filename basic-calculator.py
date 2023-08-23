def geraLinha():
    print("=" * 18)


def operationNums(num1, num2, operator):
    rsl = int

    if opt != 2:
        if operator == "+":
            rsl = num1 + num2
        elif operator == "-":
            rsl = num1 - num2
        elif operator == "*":
            rsl = num1 * num2
        elif operator == "/":
            rsl = num1 / num2

    print("\nA operação {} {} {} resulta em {}!".format(num1, operator, num2, rsl))


# Início do programa
geraLinha()
print("== Calculadora ===")
geraLinha()

opt = int

while opt :
    num1 = int(input("\n Digite o 1º número: "))
    num2 = int(input("\n Digite o 2º número: "))
    operator = input("\n Digite o operador lógico: ")
    operationNums(num1, num2, operator)

    if opt == 1 or opt == 2:
      opt = input("\nDeseja efetuar outra operação? (1-SIM ou 2-NÃO): ")
      return confirmation = True
    else:
      opt = input("\nOpção inválida! Deseja efetuar outra operação? (1-SIM ou 2-NÃO): ")

print("*** FIM DO PROGRAMA ***")

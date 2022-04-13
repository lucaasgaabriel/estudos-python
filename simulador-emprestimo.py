print("=======================")
print("Simulador de empréstimo")
print("=======================")

valorCasa = float(input("Digite o valor da casa a ser financiada: "))
salario = float(input("Digite o valor do seu salário: "))
prazoAnos = int(input("Digite em quantos anos deseja pagar: "))

prazoMensal = prazoAnos * 12

prestacao = valorCasa / (prazoAnos * 12)

aprovacao = (salario * 30)/100

if prestacao <= aprovacao:

    print("O valor financiado que deverá ser pago é de R${:.2f} por {} meses".format(prestacao, prazoMensal))

else:

    print("Empréstimo negado, pois excede 30% do seu salário")

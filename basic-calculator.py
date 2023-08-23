def geraLinha():
  print("="*18)


geraLinha()
print("== Calculadora ===")
geraLinha()


opt = str


while opt != "2":
  n1 = int(input("\n Digite o 1º número: "))
  n2 = int(input("\n Digite o 2º número: "))
  opr = input("\n Digite o operador lógico: ")
  rslt = 0

  if(opr == "+"):
    rslt = n1 + n2
  elif(opr == "-"):
    rslt = n1 - n2
  elif(opr == "*"):
    rslt = n1 * n2
  elif(opr == "/"):
    rslt = n1 / n2

  print("\nA operação {} {} {} resulta em {}!".format(n1, opr, n2, rslt))

  opt = input("\nDeseja efetuar outra operação? (1-SIM ou 2-NÃO): ")

print("*** FIM DO PROGRAMA ***")

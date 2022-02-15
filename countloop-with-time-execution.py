import time
import timeit

print("==========================================")
print("----Loop Counter With Time Execution------")
print("==========================================")

contador = 1
max_contador = int(input("Digite um número para fazer a contagem: "))

def timer():
    for i in range(1, max_contador):
        time.sleep(1)

inicio = timeit.default_timer()

while (max_contador >= contador):
    print(contador)

    contador += 1


fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print("_________")

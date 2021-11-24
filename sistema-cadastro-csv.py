header = ['nome', 'idade']
dados = []
opt = input('O que deseja fazer?\n 1- Cadastrar\n 0- Sair\n')

while opt != '0':
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    dados.append([nome, idade])
    opt = input('O que deseja fazer?\n 1- Cadastrar\n 0- Sair\n')
    
print(dados)

with open('users.csv', 'w', newline ='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)
    
with open('users.csv', 'r') as csv_file:
    csv.reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

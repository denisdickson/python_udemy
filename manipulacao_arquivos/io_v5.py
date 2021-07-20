#!Python3
#Lê arquivo 
with open('pessoas.csv') as arquivo: # abre csv pessoas
    with open('pessoas.txt', 'w') as saida: # abre pessoas.txt com função de escrita 
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado')

if saida.closed:
    print('Arquivo de saída já foi fechado')

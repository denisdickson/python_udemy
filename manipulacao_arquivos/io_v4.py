#!Python3

# Espaços corrigidos na saída
#
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado')

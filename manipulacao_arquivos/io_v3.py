#!Python3

# Espaços corrigidos na saída
#

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass            # se tiver erro, continua
finally:
    print("finaly")
    arquivo.close()


if arquivo.closed:
    print('Arquivo já foi fechado')

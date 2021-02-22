# while True:
#   print('vai demorar mto')

from random import randint

numeroInformado = -1
numeroSecreto = randint(0, 100)

while numeroInformado != numeroSecreto:
    numeroInformado = int(input('Informe o numero: '))

print('Numero secreto {} foi encontrado!'.format(numeroSecreto))

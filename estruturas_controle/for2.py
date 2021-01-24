palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end='')
print('\nFim', end='\n')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    #print(posicao + 1, nome)
    print(f'{posicao + 1})', nome)

diasSemana = ('Domingo', 'Segunda', 'Terça',
              'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in diasSemana:
    print(f'Hoje é {dia}')

# for letra in set ('muitolegal'):
#    print(letra)


for numero in {1, 2, 3, 4, 5, 6, }:
    print(numero)

#!Python3
import csv
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('nome: {},  Idade: {}'.format(*pessoa))

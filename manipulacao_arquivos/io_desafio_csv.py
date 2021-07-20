#!/usr/local/bin/python3

#Import csv e request 
import csv  
from urllib import request


def read(url):
    with request.urlopen(url) as entrada: #Requisição feita dentro de bloco with como entrada
        print('Baixando CSV ... ')# 
        dados = entrada.read().decode('latin1') #leitura da entrada usando decode latin ISO88591 ler arquivos com acentos
        print('Download completo!')#Armazenado em dados 
        for cidade in csv.reader(dados.splitlines()):#Ler cada linhas 
            print(f'{cidade[8]}: {cidade[2]}')#Imprime nona e quarta coluna


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
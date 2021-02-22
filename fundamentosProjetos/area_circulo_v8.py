#!python3
from math import pi
# função é um algoritmo com um nome , usado para evitar código duplicado


def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    raio = input('informe o raio: ')
    circulo(raio)
    area = circulo(raio)
    print('Área do Circulo', area)
    

#!python3
from math import pi
import sys
import errno
# função é um algoritmo com um nome , usado para evitar código duplicado


def help():
    print("É necessário informar o raio do circulo")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('o raio deve ser um valor numerico')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do Circulo', area)

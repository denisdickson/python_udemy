#!python3
def faixaEtaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 50):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade invalida'


if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}:{faixaEtaria(idade)}')

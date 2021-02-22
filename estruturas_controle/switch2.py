# exercicio função que retorna se é dia util ou final de semana
def getTipoDia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia util',
        3: 'Dia util',
        4: 'Dia util',
        5: 'Dia util',
        6: 'Dia util',
        7: 'Fim de semana'
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia} : {getTipoDia(dia)}')

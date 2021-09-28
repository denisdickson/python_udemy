# python3
# Pega argumentos de forma generico, posicionais e nomeados.

def todos_params(*args, **kwargs):
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=2.0)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    todos_params(primeiro='João', segundo='Maria')
    todos_params('maria', primeiro="João")
    # todos_params(primeiro= 'Maria', 'João')
    # Positional argument cannot appear after keyword arguments

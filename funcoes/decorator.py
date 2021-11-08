#!python3
def log(function):
    def decorator(*args, **kwargs):
        print(f'inicio da chamada da funçao: {function.__name__}')
        print(f'args: {args}')
        print(f'Kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x,y):
    return x+y

@log
def sub(x,y):
    return x-y


if __name__ == '__main__':
    print(soma(5,3))
    print(sub(5, y=7))

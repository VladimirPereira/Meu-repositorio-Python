a = (3, 5, 7, 9)


def soma(*args):
    """
    -> Soma todos os argumentos, se for somar uma 'tupla' ou uma 'lista' coloque
    um '*' antes da variável. Ex.: soma(*variavel)
    :param args: Pode ser uma sequência (n, n1, n2, n3...)
    ou uma variável (*variável)
    :return: Retorna a soma de todos os elementos da sequência ou da variável.
    """
    total = 0
    for v in args:
        total += v
    return total


if __name__ == '__main__':
    print(soma(*a))
    print(soma(7, 5, 9, 3))


# ===============================================================================

def mult(*args):
    """
    -> Multiplica todos os argumentos, se for multiplicar uma 'tupla'
    ou uma 'lista' coloque um '*' antes da variável. Ex.: mult(*variavel)
    :param args: Pode ser uma sequência (n, n1, n2, n3...)
    ou uma variável (*variável)
    :return: Retorna a multiplicação de todos os elementos da sequência
    ou da variável.
    """
    total = 1
    for v in args:
        total *= v
    return total


if __name__ == '__main__':
    print(mult(*a))
    print(mult(7, 5, 9, 3))
# ===============================================================================

b = (3, 2.3, 4)


def nplicar(fator, *args):
    """
    -> Multiplica cada argumento pelo fator e retorna cada resultado.
    :param fator: É número que vai multiplicar cada argumento, como na tabuada.
    :param args: Pode ser um argumento, vários ou uma variável. Se for uma variável
    é preciso colocar um '*' antes.Ex.: nplicar(fator, *variável)
    :return: Retorna a multiplicação de um ou vários elementos, de uma sequência
    ou de uma variável.
    """
    resultado = ()
    for i in args:
        resultado += (i * fator,)
    return resultado


if __name__ == '__main__':
    print(nplicar(2, 7, 3.5))
    print(nplicar(2, *b))


# ===============================================================================

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

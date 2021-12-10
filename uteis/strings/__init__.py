def conta_caracter(s):
    """
    Função que conta os caracteres de uma string.
    :param s: String a ser contada
    """
    
    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(conta_caracter('pêssego'))
    print()
    print(conta_caracter('goiabada'))
#==============================================================================

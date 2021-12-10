# -*- coding: UTF-8 -*-


def line(fig, qtde):
    """
    -> Cria uma LINHA de separação.
    :param fig: são os caracteres que vão compor
    a sua linha, podem ser 1 ou mais. Ex.: '=', '=x'
    :param qtde: é a quantidade de vezes que os
    caracteres vão se repetir.
    """
    print(fig * qtde)

if __name__=='__main__':
    line('=', 30)
# =====================================================================================

def title(txt, fig, qtde):
    """
    -> Cria um CABEÇALHO centralizado entre 2 linha.
    :param txt -> Texto do cabeçalho.
    :param fig -> A figura que fará a linha. Ex.: '=', '-'.
    Apenas 1fig, 2fig('=#') não dará certo.
    :param qtde -> Se a qtde for 10 você terá 5 antes e 5 depois centralizando o txt.
    """
    print(fig * int(len(txt) + qtde))
    print(txt.center(int(len(txt) + qtde)))
    print(fig * int(len(txt) + qtde))

if __name__=='__main__':
    title('Texto do Titulo', '=', 6)
# ====================================================================================

pula = 1
def pl(qtde=1):
    """
    -> Pula uma ou mais LINHAS.
    :param qtde: é a quantidade de linhas que serão puladas
    """
    for l in range(0, qtde):
        print()
pula += 1

if __name__=='__main__':
    pl()
# ====================================================================================

def moedaBR(vlr):
    """
    -> Formata um número em moeda Brasileira (R$)
    :param vlr: é o valor que será formatado. Ex.: 32.65
    :return: vai retornar R$ 32,65
    """
    return f'R$ {vlr:_.2f}'.replace('.', ',').replace('_', '.')

if __name__=='__main__':
    print(moedaBR(2345.97))
# =====================================================================================

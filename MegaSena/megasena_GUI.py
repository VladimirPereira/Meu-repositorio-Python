from random import randint
from time import sleep
import PySimpleGUI as sg
from uteis.themesPySG import thm

sg.theme(thm['8'])

layout = [[sg.Text('Quantos jogos você quer fazer?:', font=(12)), sg.Input(size=(5, 0), key='-QTDJG-', justification='center', font=(12))],
                [sg.Button('Enter'), sg.Button('Cancelar')]
                ]

# Crie a janela
jnl = sg.Window('PALPITES PARA A MEGA SENA', layout)
lista = list()
jogos = []
# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = jnl.read()
    # se o usuário fechar a janela ou clicar em cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    numjogos = int(values['-QTDJG-'])
    layout_01 = [[sg.Text(f'Sorteando {numjogos} jogos...')],
                [sg.Text('Boa sorte!')],
                [sg.Button('Sair')]]
    jnl_01 = sg.Window('PALPITES PARA A MEGA SENA', layout_01)
    while True:
        event, values = jnl_01.read()
    # se o usuário fechar a janela ou clicar em cancelar
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
    tot = 1
    while tot <= numjogos:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}: {l}')
        sleep(1.5)
    
    jnl.close()

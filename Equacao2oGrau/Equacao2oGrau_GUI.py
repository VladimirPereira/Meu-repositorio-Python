''' Equacao do Segundo Grau '''

import PySimpleGUI as sg
import math

class Tela:
    sg.theme('DarkAmber')
    def __init__(self):
        layout = [
            [sg.Text('Digite os valores de a, b, c:\n', font=("Helvetica", 20))],
            [sg.Text('a', font=("Helvetica", 20)), sg.Input(size=(5, 0), key='-A-', font=("Helvetica", 20)), sg.Text('b', font=("Helvetica", 20)), sg.Input(size=(5, 0), key='-B-', font=("Helvetica", 20)), sg.Text('c', font=("Helvetica", 20)), sg.Input(size=(5, 0), key='-C-', font=("Helvetica", 20))],
            [sg.Text('')],
            [sg.Button('Calcular', size=(10, 0), font=("Helvetica", 15)), sg.Exit('Sair', size=(10, 0), font=("Helvetica", 15))],
            [sg.Output(size=(60, 10), key='_output_', font=("Helvetica", 15))]
        ]
        self.jnl = sg.Window('Equação do Segundo Grau').layout(layout)
        #self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button, self.values = self.jnl.Read()
            self.jnl.FindElement('_output_').Update('')
            a = int(self.values['-A-'])
            b = int(self.values['-B-'])
            c = int(self.values['-C-'])
            print()
            print(f'a = {a}   b = {b}   c = {c}')

            d = math.pow(b, 2) - 4 * a * c
            print()
            print(f'Delta = {d}\n')

            if (d >= 0):
                x1 = (-b + math.sqrt(d)) / 2 * a
                print(f"x' = {x1:.2f}")
                x2 = (-b - math.sqrt(d)) / 2 * a
                print(f'x" = {x2:.2f}\n')
                if (d > 0):
                    print('Delta > 0.  A equação tem duas raizes reais e distintas.')
                elif (d == 0):
                    print('Delta = 0.  A equação tem duas raizes reais e iguais, ou uma única raiz.')

            else:
                print('Delta < 0.  Não existe raiz quadrada de número negativo, não há raizes.')

tela = Tela()
tela.Iniciar()

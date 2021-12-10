# PALPITES PARA A MEGA SENA

from random import randint
from time import sleep

lista = list()
jogos = []

print('=' * 35)
print('PALPITES PARA A MEGA SENA')
print('=' * 35)
numjogos = int(input('Quantos jogos você quer fazer? '))
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
print()
print('=' * 8, f'SORTEANDO {numjogos} JOGOS', '=' * 8)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1.5)
print()
print('=' * 10, '< BOA SORTE! >', '=' * 10)

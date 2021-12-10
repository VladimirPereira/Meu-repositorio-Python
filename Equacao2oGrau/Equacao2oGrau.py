''' Equacao do Segundo Grau '''


import math

print()
print("----- Equação do Segundo Grau -----\n")

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
d = math.pow(b, 2)-4*a*c
print()
print(f'Delta = {d} \n')

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


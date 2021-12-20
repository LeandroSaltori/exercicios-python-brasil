###########################
# EstruturaSequencial
###########################
"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.

"""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
nreal = float(input('Digite um número real: '))
a = (2 * n1 ) * (n2 / 2)
b = n1 *  3 + nreal
c = nreal ** 3


print(f'O PRODUTO de {n1} é {a}.')
print(f'A soma do triplo do primeiro com o terceiro = {b}')
print (f'O terceiro elevado ao cubo é {c}')

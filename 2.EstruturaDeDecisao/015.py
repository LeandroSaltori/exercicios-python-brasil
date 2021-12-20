###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""

A = int(input('Digite o valor do lado A do triangulo: '))
B = int(input('Digite o valor do lado B do triangulo: '))
C = int(input('Digite o valor do lado C do triangulo: '))


if A < B + C and B < A + C and C < B + A:
    if A == B and A == C:
        print(f'Triangulo Equilátero!')

    elif A == B or A == C or B == C:
        print(f'Triangulo Isósceles!')

    elif A != B or A != C or B != C:
        print(f'Triangulo Escaleno!')
else:
    print('Não pode formar um triangulo.')

###########################
# EstruturaDeDecisao
###########################
"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""

A = float(input('Digite o valor de A: '))


if A == 0:
    print('O valor informado é "0", a equação não é de segundo grau!\n=== FIM DO PROGRAMA ===')
else:
    B = float(input('Digite o valor de B: '))
    C = float(input('Digite o valor de C: '))
    delta = B*B - (4*A*C)
    print(delta)

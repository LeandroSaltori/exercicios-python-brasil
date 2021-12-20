###########################
# EstruturaSequencial
###########################
"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

metro = float(input('Digite a area em m² que deja pintar: '))
litros = metro / 3
lata = litros / 18
print(lata)
print(f'Você vai precisar de {lata:.2f} latas de tintas, e o valor total de sua compra é de R$ {lata * 80:.2f} reais. ')
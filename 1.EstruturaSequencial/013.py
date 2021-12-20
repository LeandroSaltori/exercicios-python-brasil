###########################
# EstruturaSequencial
###########################
"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
import locale 

def sexo():
    sexo = str(input('Informe o sexo [M/F]: ')).strip() .upper()
    while sexo not in 'MF':    
        print('Sexo inválido. Tente novamente!')
    return sexo 

peso_ideal = 0

sexo = str(input('Informe o sexo [M/F]: ')).strip() .upper()
sexo()



if sexo == 'M':
    alt = float(input('Digite sua altura: '))
    peso_ideal = (72.7*alt) - 58

else:
    alt = float(input('Digite sua altura: '))
    peso_ideal = (62.1*alt) - 44.7

print(f'Seu peso ideal é {peso_ideal:.2f}')





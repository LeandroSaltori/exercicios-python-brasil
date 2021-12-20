###########################
# EstruturaSequencial
###########################
"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tam = int(input('Digite o tamanho do arquivo (Mb): '))
veloc = int(input('Digite a velocidade do Link de internet (Mbps): '))

segundos = (tam/(veloc/8)) % 60
minutos = (tam/(veloc/8)) // 60

if minutos > 0 and segundos > 0:
    print(f'{minutos:.0f} Minutos e {segundos:.0f} Segundos.')
elif minutos == 0:
    print(f'{segundos:.0f} Segundos.')
else:
    print(f'{minutos:.0f} Minutos.')
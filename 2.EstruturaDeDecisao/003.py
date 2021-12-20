###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = str(input('Digite [M] para masculino ou [F] para Feminino [M/F]: ')).lower() .strip()

if sexo not in 'mf':
    print('Sexo inválido!')
elif sexo == 'm':
        print('M - Masculino')
elif sexo == 'f':
        print('F - Feminino') 

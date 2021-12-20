###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input('Digite uma letra: ')).strip() .lower()

if letra not in 'aeiou':
    print(f' A letra {letra}, é uma CONSOANTE')
else:
    print(f' A letra {letra}, é uma VOGAL')
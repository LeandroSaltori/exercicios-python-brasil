###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
######################################

turno = str(input('''Em qual turno você estuda:
    M - Matutino
    V - Vespertino
    N - Noturno 
RESPOSTA[M/V/N]: ''')).strip() .upper()

if turno not in 'MVN':
    print('Valor inválido!')
elif turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa noite!')

    
######################################################

turno = str(input('''Em qual turno você estuda:
    M - Matutino
    V - Vespertino
    N - Noturno 
RESPOSTA[M/V/N]: ''')).strip() .upper()

while turno not in 'MVN':
    print('Valor inválido.')
    turno = str(input('''Em qual turno você estuda:
    M - Matutino
    V - Vespertino
    N - Noturno 
RESPOSTA[M/V/N]: ''')).strip() .upper()

if turno not in 'MVN':
    print('Valor inválido!')
elif turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa noite!')
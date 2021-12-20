###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
######################################

# Solução com if:
n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))

if n1 > n2 and n2 > n3:
    print(f'{n1}, {n2}, {n3}')
if n1 > n3 and n3 > n2:
    print(f'{n1}, {n3}, {n2}')

elif n2 > n1 and n1 > n3:
    print(f'{n2}, {n1}, {n3}')
elif n2 > n3 and n3 > n1:
    print(f'{n2}, {n3}, {n1}')

elif n3 > n1 and n2> n1:
    print(f'{n3}, {n2}, {n1}')
elif n3 > n2 and n1 > n2:
    print(f'{n3}, {n1}, {n2}')

print('FIM')

#########################################

# Solução com Lista
n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))

numeros = [n1, n2, n3]
numeros.sort(reverse=-1)
print(numeros)

#########################################

# Solução for
numeros = list()
cont = 0
for n in range (1,4):
    cont += n
    n = int(input(f'Digite {n}º número: '))
    numeros.append(n)
numeros.sort(reverse=-1)
print(f'Os numeros em ordem decrescente são {numeros}')
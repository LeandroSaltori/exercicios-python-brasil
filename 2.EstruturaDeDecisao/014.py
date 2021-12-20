###########################
# EstruturaDeDecisao
###########################
"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a nota do aluno: ')) 
media = (nota1 + nota2 ) / 2
conceito = ''

if media >= 9 and media <= 10:
    conceito = 'A'
    print(f'As notas do aluno foram {nota1} e {nota2} e a media entra elas é {media}.')
    print(f'O Aluno foi APROVADO com o conceito {conceito}.')

if media >= 7.5 and media < 9:
    conceito = 'B'
    print(f'As notas do aluno foram {nota1} e {nota2} e a media entra elas é {media}.')
    print(f'O Aluno foi APROVADO com o conceito {conceito}.')

if media >= 6 and media < 7.5:
    conceito = "C"
    print(f'As notas do aluno foram {nota1} e {nota2} e a media entra elas é {media}.')
    print(f'O Aluno foi APROVADO com o conceito {conceito}.')

if media >= 4 and media < 6:
    conceito = "D"
    print(f'As notas do aluno foram {nota1} e {nota2} e a media entra elas é {media}.')
    print(f'O Aluno foi REPROVADO com o conceito {conceito}.')

if media >= 0 and media < 4:
    conceito = "E"
    print(f'As notas do aluno foram {nota1} e {nota2} e a media entra elas é {media}.')
    print(f'O Aluno foi REPROVADO com o conceito {conceito}.')
'''Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
O algoritmo deve mostrar as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

O'''

# Solicitar as duas notas do aluno
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

# Calcular a média
media = (nota1 + nota2) / 2

# Determinar o conceito e se o aluno foi aprovado ou reprovado
if 9.0 <= media <= 10.0:
    conceito = 'A'
    status = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = 'B'
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = 'C'
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = 'D'
    status = "REPROVADO"
else:
    conceito = 'E'
    status = "REPROVADO"

# Exibir as notas, a média, o conceito e o status (aprovado ou reprovado) usando .format()
print("Nota 1: {}".format(nota1))
print("Nota 2: {}".format(nota2))
print("Média: {:.2f}".format(media))
print("Conceito: {}".format(conceito))
print("Status: {}".format(status))

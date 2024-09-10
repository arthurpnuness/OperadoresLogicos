'''Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Também solicite qual a % de frequência e aula, verifique e apresente a seguinte mensagem:
Aprovado: Nota maior ou igual a 7,0 e frequência igual ou superior a 75%.
Exame: Nota maior ou igual a 4,0 e menor que 7,0 e frequência superior a 75%.
Reprovado: Nota inferior a 4,0 ou frequência menor que 75%.
'''

nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Digite a nota da sua segunda prova: '))
frequencia = float(input('Digite também a sua frequencia em aula (entre 1 a 100): '))

media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
    print('Aprovado: Nota maior ou igual a 7,0 e frequência igual ou superior a 75%.')
elif media >= 4 or media < 7 and frequencia >= 75:
    print('Exame: Nota maior ou igual a 4,0 e menor que 7,0 e frequência superior a 75%.') 
else:
    print('Reprovado: Nota inferior a 4,0 ou frequência menor que 75%.')
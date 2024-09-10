'''Crie um programa que leia o nome, o salário e o tempo de serviço de um funcionário e informe se ele tem direito a receber um aumento. O funcionário deve ter pelo menos 5 anos de serviço e o salário não pode ser superior a R$ 2.000,00 para receber o aumento de 10%. Caso contrário, o aumento é de 5%.'''

nome = input('Digite seu nome: ')
salario = float(input('Digite o teu salario: '))
tempServ = int(input('QUando tempo de serviço voce ja possui? '))

if salario <= 2000 and tempServ >= 5:
    aumento = (salario * 0.10) + salario 
    print('{} pelo tempo de serviço que voce possui conosco, voce recebeu um aumento de 10%. Parabens! Seu salario agora é R${}'.format(nome, aumento))
else:
    aumento = (salario * 0.05) + salario
    print('{} voce recebeu um aumento de 5%. Parabens! Seu salario agora é R${}'.format(nome, aumento))
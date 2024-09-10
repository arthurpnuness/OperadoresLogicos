'''Faça um script que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
lado1 = float(input('Digite o medida do primeiro lado do triangulo: '))
lado2 = float(input('Digite o medida do segundo lado do triangulo: '))
lado3 = float(input('Digite o medida do terceiro lado do triangulo: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Os lados informados formam um Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados informados formam um Triângulo Isósceles.")
    else:
        print("Os lados informados formam um Triângulo Escaleno.")
else:
    print("Os lados informados não formam um triângulo.")

'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                              Até 5 Kg                 Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''


# Solicitar a quantidade de morangos e maçãs
kgMorangos = float(input("Informe a quantidade de morangos (em Kg): "))
kgMacas = float(input("Informe a quantidade de maçãs (em Kg): "))

# Preços por Kg
precoMorangosAte5Kg = 2.50
precoMorangosAcima5Kg = 2.20
precoMacasAte5Kg = 1.80
precoMacasAcima5Kg = 1.50

# Calcular o valor dos morangos
if kgMorangos <= 5:
    valorMorangos = kgMorangos * precoMorangosAte5Kg
else:
    valorMorangos = kgMorangos * precoMorangosAcima5Kg

# Calcular o valor das maçãs
if kgMacas <= 5:
    valorMacas = kgMacas * precoMacasAte5Kg
else:
    valorMacas = kgMacas * precoMacasAcima5Kg

# Calcular o valor total da compra
valorTotal = valorMorangos + valorMacas

# Aplicar o desconto se a condição for atendida
if kgMorangos + kgMacas > 8 or valorTotal > 25:
    valorTotal *= 0.90  # Aplicar desconto de 10%

# Exibir o valor a ser pago
print("Valor a ser pago: R$ {:.2f}".format(valorTotal))

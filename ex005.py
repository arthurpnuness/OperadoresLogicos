'''Faça um script que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O script deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

# Inicializar contador de respostas "sim"
respostas_positivas = 0

# Inicializar contador para controlar o loop
contador = 0

# Fazer as perguntas com o loop while
while contador < 5:
    if contador == 0:
        resposta = input("Telefonou para a vítima? (sim/não): ").lower()
    elif contador == 1:
        resposta = input("Esteve no local do crime? (sim/não): ").lower()
    elif contador == 2:
        resposta = input("Mora perto da vítima? (sim/não): ").lower()
    elif contador == 3:
        resposta = input("Devia para a vítima? (sim/não): ").lower()
    elif contador == 4:
        resposta = input("Já trabalhou com a vítima? (sim/não): ").lower()
    
    # Verificar se a resposta é "sim"
    if resposta == "sim":
        respostas_positivas += 1
    
    # Aumentar o contador para passar para a próxima pergunta
    contador += 1

# Verificar a classificação com base nas respostas "sim"
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Mostrar o resultado final
print("Classificação: {}".format(classificacao))

# Condicional If (Se)
if 5 > 2:
    print('A sentença é verdadeira!')
print()

# Condicional If...Else
if 5 < 2:
    print('A sentença é verdadeira!')
else:
    print('A sentença é Falsa!')
print()

# Condicional If...Else com variável
dia = 'Terça'
if dia == 'Segunda':
    print('Hoje fará sol!')
else:
    print('Hoje vai Chover!')
    print()

# Podemos usar o operador elif para validar mais de uma condição
dia = 'Terça'
if dia == "Segunda":
    print('Hoje fará sol!')
elif dia == 'Terça':
    print('Hoje vai Chover!')
else:
    print('Sem previsão do tempo para o dia selecionado')
print()
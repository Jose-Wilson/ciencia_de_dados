from platform import python_version

print(f'Versão do Python {python_version()}')
print()

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.insert(2, 110)
print(cidades)
print()

cidades.remove('Salvador')
print(cidades)
print()

cidades.reverse()
print(cidades)
print()

x = [3, 4, 6, 1, 2, 30, 25]
x.sort()
print(x)

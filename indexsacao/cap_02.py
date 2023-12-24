from platform import python_version

print(python_version())
print()

primos = []

for num in range(0, 50):
    eh_primos = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primos = False
            break
        i += 1
    if eh_primos:
        primos.append(num)
print(primos)

numeros = [16, 4, 9, 1, 3, 20, 8]
for i in range(len(numeros)):
    for j in range(len(numeros)-i-1):
        if numeros[j]>numeros[j+1]:
            numeros[j],numeros[j+1]=numeros[j+1],numeros[j]
print(numeros)
positivos = 0
negativos = 0
neutros = 0

for i in range(3):
    numero = float(input("Digite un número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos +=1
    else:
        neutros +=1

print("Números positivos: ",positivos)
print("Números negativos: ",negativos)
print("Números neutros: ",neutros)
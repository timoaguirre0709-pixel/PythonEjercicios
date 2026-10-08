suma = 0
mayor = 0
menor = 1

for i in range(3):
    nota = float(input("Digite la calificación: "))

    suma += nota

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

promedio = suma / 3

print("Promedio: ",promedio)
print("Calificación más alta: ",mayor)
print("Calificación más baja: ",menor)
suma = 0
for i in range(3):
    numero = float(input("Digite un número negativo: "))

    positivo = abs(numero)
    suma += positivo

    print("La suma de los números positivos es: ",suma)
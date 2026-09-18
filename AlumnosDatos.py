hombres = 0
mujeres = 0
suma_alturas = 0
cantidad_alumnos = 0
mayor_170 = 0
menor_igual_150 = 0

while True:
    edad = int(input("Digite la edad (0 para terminar): "))

    if edad == 0:
        break

    sexo = input("Digite el sexo (H/M ): ").upper()
    altura = float(input("Digite la altura en metros: "))

    if sexo == "H":
        hombres += 1
    elif sexo == "M":
        mujeres += 1

        suma_alturas +=altura
        cantidad_alumnos += 1

        if altura > 1.70:
            mayor_170 +=1

        if altura <= 1.50:
            menor_igual_150 += 1

if cantidad_alumnos > 0:
    promedio_altura = suma_alturas / cantidad_alumnos
else:
    promedio_altura = 0

    print("Cantidad de hombres: ",hombres)
    print("Cantidad de mujeres: ",mujeres)
    print("Altura promedio: ",promedio_altura)
    print("Alumnos con altura mayor a 1.70m: ",mayor_170)
    print("Alumnos con altura menor o igual a 1.50m: ",menor_igual_150)
suma_hombres =0
suma_mujeres = 0
cantidad_hombres = 0
cantidad_mujeres = 0

n = int(input("Digite la cantidad de alumnos: "))

for i in range(n):
    sexo = input("Digite el sexo (H/M): ").upper()
    edad = int(input("Digite la edad: "))

    if sexo == "H":
        suma_hombres += edad
        cantidad_hombres += 1
    elif sexo == "M":
        suma_mujeres += edad
        cantidad_mujeres += 1

total_alumnos = cantidad_hombres + cantidad_mujeres
suma_total = suma_hombres + suma_mujeres

if cantidad_hombres > 0:
    print("Promedio de edad de hombres: ",suma_hombres / cantidad_hombres)

if cantidad_mujeres > 0:
    print("Promedio de edad de mujeres: ",suma_mujeres / cantidad_mujeres)

if total_alumnos > 0:
    print("Promedio de edad del grupo: ",suma_total / total_alumnos)
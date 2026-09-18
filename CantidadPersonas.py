hombres = 0
mujeres = 0

n = int(input("Digite la cantidad de personas: "))

for i in range(n):
    sexo = input("Digite el sexo (H/M): ").upper()

    if sexo =="H":
        hombres += 1
    elif sexo == "M":
        mujeres += 1

print("Cantidad de hombres: ",hombres)
print("Cantidad de mujeres: ",mujeres)
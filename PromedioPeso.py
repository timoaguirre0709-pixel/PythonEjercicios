peso_ninos = 0
peso_jovenes = 0
peso_adultos = 0
peso_ancianos = 0

cantidad_ninos = 0
cantidad_jovenes = 0
cantidad_adultos = 0
cantidad_ancianos = 0

for i in range(4):
    edad = int(input("Digite la edad: "))
    peso = float(input("Digite el peso: "))

    #Aquí van los rangos de edad de la tabla
    if edad <= 12:
        peso_ninos += peso
        cantidad_ninos +=1
    elif edad <= 29:
        peso_jovenes += peso
        cantidad_jovenes += 1
    elif edad <= 59:
        peso_adultos += peso
        cantidad_adultos += 1
    else:
        peso_ancianos += peso
        cantidad_ancianos += 1

if cantidad_ninos > 0:
    print("Promedio niños ",peso_ninos/cantidad_ninos)

if cantidad_jovenes > 0:
    print("Promedio jovenes ",peso_jovenes/cantidad_jovenes)

if cantidad_adultos > 0:
    print("Promedio adultos ",peso_adultos/cantidad_adultos)

if cantidad_ancianos > 0:
    print("Promedio ancianos ",peso_ancianos/cantidad_ancianos)


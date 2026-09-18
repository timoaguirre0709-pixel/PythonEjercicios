menor_50 = 0
entre_50_69 = 0
entre_70_79 = 0
mayor_igual_80 = 0

for i in range(23):
    nota = float(input("Digite la calificación (1-100): "))

    while nota < 1 or nota > 100:
        print("La calificación debe estar entre 1 y 100.")
        nota = float(input("Digite nuevamente la calificación: "))

        if nota < 50:
            menor_50 += 1
        elif nota < 70:
            entre_50_69 += 1
        elif nota < 80:
            entre_70_79 += 1
        else:
            mayor_igual_80 += 1

            print("Menos de 50: ",menor_50)
            print("De 50 a 69: ",entre_50_69)
            print("De 70 a 79: ",entre_70_79)
            print("De 80 a 100: ",mayor_igual_80)
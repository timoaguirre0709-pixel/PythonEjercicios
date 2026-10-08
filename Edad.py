from datetime import date
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
ano_actual = date.today().year
edad = ano_actual - ano_nacimiento
print("Su edad es: ",edad, "años")

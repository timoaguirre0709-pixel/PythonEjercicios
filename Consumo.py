kilometros = float(input("Ingrese los kilómetros recorridos: "))
litros = float(input("Ingrese los litros de gasolina utilizados: "))

if litros > 0:
    consumo = kilometros / litros
    print("El consumo es de ",consumo, "km por litro")
else:
    print("La cantidad de litros debe ser mayor que cero")
precio = float(input("Ingrese el precio del producto: "))
porcentaje_iva = 19
iva = precio * porcentaje_iva / 100
total = precio + iva
print("El valor del IVA es: ",iva)
print("El precio total con IVA es: ",total)
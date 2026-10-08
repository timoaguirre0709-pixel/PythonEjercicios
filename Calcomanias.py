amarillas = 0
azules = 0
rojas = 0
verdes = 0
rosas = 0

n = int(input("Digite la cantidad de carros: "))

for i in range(n):
    digito = int(input("Digite el último digito de la placa: "))

    if digito in [1, 2]:
        amarillas += 1
    elif digito in [3, 4]:
        rosas += 1
    elif digito in [5, 6]:
        rojas += 1
    elif digito in [7, 8]:
        verdes += 1
    elif digito in [9, 0]:
        azules +=1

print("Calcomanias amarillas: ",amarillas)
print("Calcomanias rosas: ",rosas)
print("Calcomanias rojass: ",rojas)
print("Calcomanias verdes: ",verdes)
print("Calcomanias azules: ",azules)
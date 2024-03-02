ha=int(input("Ingrese la hora actual (en formato de 24 horas): "))
has=int(input("Ingrese la cantidad de horas que desea sumar: "))
hf=(ha + has)%24
print(f"Dentro de {has} horas seran las {hf}")
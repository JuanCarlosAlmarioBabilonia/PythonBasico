a=int(input("Ingrese el dividendo: "))
b=int(input("Ingrese el divisor: "))
x=int(a/b)
y=a%b
if y==0:
    print("La division es exacta")
    print(f"Cociente: {x}")
    print(f"Residuo: {y}")
else:
    print("La division no es exacta")
    print(f"Cociente: {x}")
    print(f"Residuo: {y}")
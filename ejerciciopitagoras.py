c1=float(input("Ingrese el valor del cateto a: "))
c2=float(input("Ingrese el valor del cateto b: "))
from math import sqrt
hipa=sqrt((c1**2 + c2**2))
print(f"El valor de la hipotenusa dados los catetos es {hipa}")
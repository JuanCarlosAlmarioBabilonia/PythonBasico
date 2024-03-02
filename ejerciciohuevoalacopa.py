temp=float(input("Ingrese la temperatura original del huevo: "))
from math import log
from math import pi
mp=47
mg=67
p=1.038
c=3.7
k=5.4*10**-3
n1=(mp**(2/3) * c * p**(1/3))
n2=(k * pi**2 * (4*pi/3)**(2/3))
n3= log ((0.76 * ((temp-100) / (70-100))))
t=((n1/n2)/n3)
tm=(t/60)
print(f"El tiempo maximo para prepararlo a la copa son: {t} segundos o {tm} minutos")
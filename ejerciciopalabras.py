p1=input("Ingrese la primera palabra: ")
p2=input("Ingrese la segunda palabra: ")
lp1=len(p1)
lp2=len(p2)
difa=lp1-lp2
difb=lp2-lp1
if lp1==lp2:
    print(f"Las palabras {p1} y {p2} tienen la misma cantidad de letras")
else:
    if lp1>lp2:
        print(f"La palabra {p1} es mas larga que la palabra {p2} por {difa} letra(s)")
    else:
        print(f"La palabra {p2} es mas larga que la palabra {p1} por {difb} letra(s)")

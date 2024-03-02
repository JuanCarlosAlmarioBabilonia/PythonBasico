a=int(input("Ingrese los juegos ganados por A: "))
b=int(input("Ingrese los juegos ganados por B: "))
if 0<a<=5 and 0<b<=5:
    print ("El juego no ha terminado")
elif 5<=a<=7 and 5<=b<=7:
    if a==7:
        print("El jugador A gano el juego")
    elif b==7:
        print("El jugador B gano el juego")
    else:
        print("EL juego no ha terminado")
elif a==6 and 0<=b<5:
    print("El jugador A gano el juego")
elif b==6 and 0<=a<5:
    print("El jugador B gano el juego")
else:
    print("El juego es invalido")
#from time import localtime
# t=localtime()
diahoy=2
meshoy=3
añohoy=2024
print("Ingrese su fecha de nacimiento")
dia=int(input("Dia: "))
mes=int(input("Mes: "))
año=int(input("Mes: "))
age=(añohoy-año)
if dia>diahoy and mes>meshoy:
    print (f"Usted tiene {age-1} años")
else:
    if dia>diahoy and mes<meshoy:
        print(f"Usted tiene {age} años")
    else:
        if dia<diahoy and mes<meshoy:
            print (f"Usted tiene {age} años")
        else: 
            if dia<diahoy and mes>meshoy:
                print (f"Usted tiene {age-1} años")
            else:
                if dia==diahoy and mes==meshoy:
                    print (f"Usted tiene {age} años")
año=int(input("Ingrese el año: "))
if año%400==0:
    print(f"El año {año} es bisiesto")
else:
    if año%100==0 and año%400!=0:
        print(f"El año {año} no es bisiesto")
    else:
        if año%4==0 and año%100!=0:
            print(f"El año {año} es bisiesto")
        else:
            if año%4!=0:
                print(f"El año {año} no es bisiesto")
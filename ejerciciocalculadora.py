print("Calculadora")
print("Ingrese dos valores numericos: ")
v1=float(input())
v2=float(input())
print ("Ingrese el simbolo de la operacion que desea hacer (+ (suma), - (resta), * (multiplicacion), / (division) o ** (potenciacion)")
opc=input()
if opc== "+":
    res=v1+v2
    print(f"{v1} {opc} {v2} = {res}")
else: 
    if opc== "-":
        rez=v1-v2
        print(f"{v1} {opc} {v2} = {rez}")
    else:
        if opc== "*":
            rep=v1*v2
            print(f"{v1} {opc} {v2} = {rep}")
        else:
            if opc== "/":
                ren=v1/v2
                print(f"{v1} {opc} {v2} = {ren}")
            else:
                if opc== "**":
                    rem=v1**v2
                    print(f"{v1} {opc} {v2} = {rem}")


num=int(input("Ingrese el numero de tres cifras que desea invertir: "))
d1=num//100
d2=(num%100)//10
d3=num%10
res=(d3*100)+(d2*10)+d1
print(f"El numero invertido de {num} es {res}")
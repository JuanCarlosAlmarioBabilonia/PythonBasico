nc1=int(input("Ingrese su nota del certamen 1: "))
nc2=int(input("Ingrese su nota del certamen 2: "))
lab=int(input("Ingrese su nota de laboratorio: "))
labn=lab*0.3
nbc=60-labn
nc=nbc/0.7
npc=(nc1+nc2)/3
nc3=(nc*3)-(nc1+nc2)
ntc=(nc1+nc2+nc3)/3
npac=ntc*0.7
nc=npc*0.7
nr=int(nc+labn)
npr=int(npac+labn)
if nr>=60:
    print(f"¡Ya pasaste el ramo con {nr}!")
else:
    if nc3<=100:
       print(f"Debes sacar minimo", int(nc3),f"en el certamen 3 para aprobar el ramo con {npr}")   
    else:
       print (f"No tienes oportunidad de pasar el ramo, ni con nota de 100 en el certamen 3")
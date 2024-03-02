def ordnums (n1, n2):
    nums = [n1, n2]
    nums.sort()
    return nums
print("Orden de dos numeros")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
numord=ordnums(num1, num2)
print("Los numeros ordenados de menor a mayor son:", numord)
print()

def ordnums (n1, n2, n3):
    nums = [n1, n2, n3]
    nums.sort()
    return nums
print("Orden de tres numeros")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
numord=ordnums(num1, num2, num3)
print("Los numeros ordenados de menor a mayor son:", numord)
print()

def ordnums (n1, n2, n3, n4):
    nums = [n1, n2, n3, n4]
    nums.sort()
    return nums
print("Orden de cuatro numeros")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
num4=int(input("Ingrese el cuarto numero: "))
numord=ordnums(num1, num2, num3, num4)
print("Los numeros ordenados de menor a mayor son:", numord)


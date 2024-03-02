def detcar(caracter):
    if caracter.isalpha():
        if caracter.isupper():
            print("La letra ingresada es mayuscula")
        else:
            print("La letra ingresada es minuscula") 
    elif caracter.isdigit():
        print("El caracter ingresado es un número.")
    else:
        print("El caracter ingresado no es ni letra ni número.")
caracter=input("Ingrese un caracter: ")
detcar(caracter)

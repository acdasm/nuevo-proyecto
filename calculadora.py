print("********************************************")
print("CALCULADORA.")
print("********************************************")
print("MENU")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACION")
print("4. DIVISION")

numero = int(input("Elije: "))
if numero ==1:
    print("Elejiste suma")
    numero = int(input("Inroduce el primer valor: "))
    numero += int(input("Inroduce el segundo valor: "))
    print("El resultado de la suma es", numero)
elif numero ==2:
    print("Elejiste resta")
    numero = int(input("Inroduce el primer valor: "))
    numero -= int(input("Inroduce el segundo valor: "))
    print("El resultado de la resta es", numero)
elif numero ==3:
    print("Elejiste multiplicacion")
    numero = int(input("Inroduce el primer valor: "))
    numero *= int(input("Inroduce el segundo valor: "))
    print("El resultado de la multiplicacion es", numero)
elif numero ==4:
    print("Elejiste division")
    numero = int(input("Inroduce el primer valor: "))
    numero //= int(input("Inroduce el segundo valor: "))
    print("El resultado de la division es", numero)
else:
    print("La opcion seleccionada no existe. ")

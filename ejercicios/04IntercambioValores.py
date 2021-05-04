'''
En este tutorial vamos a Intercambio de valores de dos variables, osea que vamos a pedirle al usuario que ingrese dos valores a y b y nuestro programa colocará el valor de a en b y el valor de b en a.
'''

print("Humano ingresa los valores que se te piden a continuación")
a=int(input("El valor de a:"))
b=int(input("El valor de b:"))
aux=a
a=b
b=aux
print("Humano aqui estan tus valores")
print(f"Valor a{a}")
print(f"Valor b{b}")
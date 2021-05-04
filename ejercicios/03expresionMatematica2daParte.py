'''
En este tutorial vamos a:
- Convertir una expresión matemática en código de python.
- Redondear números decimales a mostrar con las funciones de f-string de python.
'''
a=float(input("Ingresa el valor de a: "))
b=float(input("Ingresa el valor de b: "))
c=float(input("Ingresa el valor de c: "))
d=float(input("Ingresa el valor de d: "))
e=float(input("Ingresa el valor de e: "))
f=float(input("Ingresa el valor de f: "))
res=(a+b/c) / (d+e/f)
print(f"Humano aqui está tu resultado:{res:,.3f}")
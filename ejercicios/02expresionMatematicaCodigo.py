'''
En este tutorial vamos a:
- Convertir una expresión matemática en código de python.
- Redondear números decimales a mostrar con las funciones de f-string de python.
'''

a=float(input("Humano ingresa el valor de a:"))
b=float(input("Humano ingresa el valor de b:"))
res=a/b+1
print(f"Humano aqui esta tu resultado:{res:,.2f}")
''' Una variable es una palabra que puede almacenar algún tipo de dato y python maneja 3 tipos de datos:
Número
Coma flotante
Texto
Booleano: Falso o Verdadero
Además vamos a aprender el tipado dinámico.'''

#Declaramos e imprimimos una variable de tipo numero
numero=10
print (numero)
print(type(numero))
print("----------")
#Declaramos e imprimimos una variable de tipo coma flotante
numeroComaFlotante=10.25
print (numeroComaFlotante)
print(type(numeroComaFlotante))
print("----------")
#Declaramos e imprimimos una variable de tipo string
texto="Hola soy una serpiente 🐍"
print (texto)
print(type(texto))
print("----------")
#Declaramos e imprimimos una variable de tipo booleano
booleano=True
print (booleano)
print(type(booleano))
print("----------")
#Declaramos e imprimimos tipado dinámico
suma=numero+numeroComaFlotante
print(suma)
print(type(suma))
print("----------")
suma=texto
print(suma)
print(type(suma))
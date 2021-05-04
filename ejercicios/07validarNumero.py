x=float(input("Humano ingresa el valor de x: "))
y=float(input("Humano ingresa el valor de y: "))
dividendo=(y**2)-1
if dividendo!=0:
    res= ( x**(1/2) ) / dividendo
    print(f"Humano aqui está tu inche resultado:{res}")
else:
    print(f"Humanito el valor de 'Y' no puede ser {y}")

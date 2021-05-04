'''
En este tutorial vamos a calcular las calificaciones de un alumno con las siguientes características:
Calificación de prácticas que es 40%.
Calificación de participación que es 20%.
Calificación de examen que es 40%.
Obtener la calificación final sumando y obteniendo el promedio.
'''
print("Humano por favor ingresa las calificaciones del alumno:")
practicas=float(input("Calificación de las prácticas:"))
participacion=float(input("Calificación de las participaciones:"))
examen=float(input("Calificación del exámen:"))
practicas*=0.40
participacion*=0.20
examen*=0.40
final=practicas+participacion+examen
print(f"Esta es la calificacion del alumno:{final:.2f}")
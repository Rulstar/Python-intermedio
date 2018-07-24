#-*-coding:utf-8-*-
#Ejemplo 1.- Clase y objeto
class Curso:
    #Atributos
    nombre="Python intermedio"
    duracion=5
c=Curso()
print("Curso de " + c.nombre); print("La duración del curso es de " + str(c.duracion) + " días")
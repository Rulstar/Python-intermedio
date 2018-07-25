#-*-coding:utf-8-*-
'''
class Curso:
    #Abstracción de datos
    nombre="Python intermedio"
    duracion=5
    #Abstracción Funcional son las acciones que va a hacer la clase
    def cambiarNombre(self, nuevoNombre): #el self va a tener el valor cuando el objeto esté creado
        self.nombre=nuevoNombre
#Objeto 1
c=Curso()
print("Curso de " + c.nombre); print("La duración del curso es de " + str(c.duracion) + " días.")
c.cambiarNombre("Python avanzado")
print("Curso de " + c.nombre)
print("Curso de " + Curso.nombre)
#objeto 2
c2=Curso()
print("Curso de " + c2.nombre)
c2.cambiarNombre("Python super avanzado :)")
print("Curso de " + c2.nombre)
'''
# -*- coding:utf-8 -*-
'''
class Humano():
    #Constructor
    def __init__(self, nombre, edad, genero, calificacion):
        #Abstracción de Datos
        self.__nombre=nombre #Atributo privado
        self.__edad=edad #Atributo privado
        self.__genero=genero #Atributo privado
        self.calificacion=calificacion #Atributo público
        self.__miMetodoPrivado()
    #Abstracción funcional
    #Get (obtener el valor de una variable) - Set (cambiar el valor de una variable)
    #Métodos públicos
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getGenero(self):
        return self.__genero
    def getCalificacion(self):
        return self.calificacion
    def setNombre(self, nombre=None):
        self.__nombre=nombre
    def setEdad(self, edad=None):
        self.__edad=edad
    def setGenero(self, genero=None):
        self.__genero=genero
    def setCalificacion(self, calificacion=None):
        self.calificacion=calificacion
    #Metodo privado (sólo se consulta dentro del objeto)
    def __miMetodoPrivado(self):
        print("Creando un humano")
#Creación de un objeto humano
nombre=input("Introduzca el nombre: ")
edad=int(input("Dame la edad: "))
genero=input("Género M/H: ")
calificacion=int(input("Calificación: "))
h1=Humano(nombre, edad, genero, calificacion)
#h1.__miMetodoPrivado() #no se puede acceder porque es un método privado
print(h1.getNombre())
'''
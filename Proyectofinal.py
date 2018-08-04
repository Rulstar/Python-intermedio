# -*- coding:utf-8 -*-
class Practica:
    #Constructor
    #Abstracción de datos
    def __init__(self, nombre, num_experi, num_datos, elaborada):
        self.nombre=nombre
        self.num_experi=num_experi
        self.num_datos=num_datos
        self.__elaborada=False
    #Abstracción funcional
    def descripcion(self):
        print("Nombre de la práctica: " + self.nombre + "\nExperimentos elaborados: " + str(self.num_experi) + "\nDatos a colocar: " + str(self.num_datos))
    def introducir(self):
        print("Introdujo datos.")
class Termodinamica(Practica):
    def __init__(self, nombre):
        Practica.__init__(self, nombre, 3, 15, True)
class Gravitacion(Practica):
    def __init__(self, nombre):
        Practica.__init__(self, nombre, 4, 25, True)
#Creación de objetos
calefaccion=Termodinamica("Lo que pasa en un horno de microondas.")
calefaccion.descripcion()
nombre=input("Nombre de la práctica: ")
newton=Gravitacion(nombre)
newton.descripcion()
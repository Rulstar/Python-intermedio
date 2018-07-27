# -*- coding:utf-8 -*-
class Practica:
    #Constructor
    #Abstracción de datos
    def __init__(self, nombre, num_experi, num_datos, incertidumbres, elaborada):
        self.nombre=nombre
        self.num_experi=num_experi
        self.num_datos=num_datos
        self.incertidumbres=incertidumbres
        self.__elaborada=False
        self.__calculoIn()
        self.__imprimir()
    #Abstracción funcional
    def descripcion(self):
        print("Nombre de la práctica: " + self.nombre + "\nExperimentos elaborados: " + self.num_experi + "\nDatos a colocar: " + self.num_datos + "\nIncertidumbre por calcular: " + self.incertidumbres)
    def introducir(self):

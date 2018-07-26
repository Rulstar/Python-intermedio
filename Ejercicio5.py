# -*- coding:utf-8 -*-
#EJEMPLO DE HERENCIA
#Creación de clase Animal
class Animal():
    #Abstracción de datos
    #Constructor
    def __init__(self, nombre, num_patas):
        self.__num_patas=num_patas #Encapsulamiento
        self.__nombre=nombre
        self.alimento=0
    #Abstracción Funcional
    def comer(self):
        self.alimento=self.alimento+1 #nivel de variables
        #self.alimento+=1 #nivel de bits
        print(self.__nombre + " ha comido " + str(self.alimento) + " raciones.")
    def comer2(self, num):
        self.alimento=self.alimento + num
        print(self.__nombre + " ha comido " + str(self.alimento) + " raciones.")
#Herencia
class Perrito(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre, 4) #Polimorfismo
class Avestruz(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre, 2)
#Creación de objetos
terry=Perrito("Terry")
terry.comer() #Reutiliza el código
nombre=input("Nombre del avestruz: ")
pancho_venancio=Avestruz(nombre)
#pancho_venancio.comer()
comida=int(input("Dame el número de raciones, por favor: "))
pancho_venancio.comer2(comida)

#Repaso:
#Ejemplo 1:
'''
Comentario de varias líneas
'''
#print("Organización") #Python3
#print"Organización" #Python2

#Saber si un número es mayor o menor a 10
#a=int(input("Dame un número: ")) #Python3
#a=raw_input("Dame tu nombre: ") #Python2
#print(1==10)
#if(a>10):
#    print("Es mayor a 10")
#else:
#    print("Es menor a 10")

#Saber si una persona es mayor o menor de edad
#Opción 1.-
#a=int(input("Dame tu edad: "))
#while a<=0 or a>=100:
#    print("No estas en el intervalo de edades, vuelve a intentarlo")
#    a=int(input("Dame tu edad: "))
#if(a>=18):
#    print("Eres mayor de edad")
#else:
#    print("Eres un bebito")

#Opción 2.-
#b=int(input("Introduce tu edad: "))
#c=18
#while b<=c:
#    print("Eres menor de edad, no puedes entrar")
#    b=int(input("Introduce tu edad: "))
#print("Edad admitida, puedes ingresar")

#Imprimir del 1 al 10.
#a=1
#while a<=10:
#    print(a)
#    a=a+1

#Validar contraseña.
#b=int(input("Introduce tu contraseña: "))
#c=1234
#while b!=c:
#    print("Contraseña Incorrecta")
#    b=int(input("Introduce tu contraseña: "))
#print("Contraseña correcta, puedes ingresar")

#Listas
#Opción 1.-
#lista=['1', 2, False, 10.0, 1]
#for i in lista:
#    print(i)

#Opción 2.-
#lista=['1', 2, False, 10.0, 1]
#for j in range(0,5): #nos imprime uno antes del último
#    print(lista[j])

#Funciones
#def suma(a, b):
#    c=a+b
#    return c
#r=suma(9, 1)
#print(r) #ó
#print(suma(9, 1)) #para avanzados
# -*- coding:utf-8 -*-
#f=open("archivo_Myl.txt", "w") #se pone la ruta del archivo
#f.write("Linea 1 \n")
##Listas de cadenas para escribir en el archivo
#lineas=["Linea 2\n", "Linea 3\n"]
##Escribir varias lineas
#f.writelines(lineas)
#f.close()


#Leer un archivo y te lo imrpime en consola
#f=open("archivo_Myl.txt", "r")
#lineal=f.readlines() #variable de lista
#print(lineal)
#f.close

a="Temp: 10 C"
print(a)
print(a.find("Temp")) #imprime la posición donde empieza la letra
indice=a.find("Temp")
print(a[indice+5:-2]) #imprime lo que tiene "a", desde donde hasta donde le indicas
#print(a[indice+6:indice+8])
#Manejo de listas dinámicas
temp=a[indice+5:-2]
lista=list()
lista.append(temp)
print(lista)
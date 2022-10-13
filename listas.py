# Listas

#crear una lista, va entre []

lista1 = [12, "holi", "hola", "chau", 12.5, True]

hola= "hola"
lista2 = list(hola)

print (lista1)
print (lista2)

# como acceder un elemento de la lista segun su indice

#formar de acceder al elemento de una lista

#nombreLista[indice]

print (lista1[2])
print (lista1[0] - lista1[4])
print (lista1)


dato_ingresado =input("ingresame un dato : ")
lista1.append(dato_ingresado)
print(lista1)

lista1[2]=input("ingresa un dato que va estar en el indice 2 : ")
print(lista1)

# tomar valor de variables

var1="Cronos"
lista3 =[var1, 2, 3, "chau"]

print (lista3)

lista1 =[1,1,True,["hola", "chau"], 1.4] #en la posicion 3 hay una lista["hola", "chau"]
lista2 = list()
lista3 = list("hola") # toma la lista y la separa por cada caracter
lista4 = [] # lista vacia
lista5 = list("5623") # los enteros no son iterables, hay ponerlo entre comillas 

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

# acceder elementos de la lsitas
oper= 4 + int (lista5[1]) #casteamos el string #6 a entero y realizamos la suma

print (oper)

elemEnLista1 = lista1[3][0] #tomo de lista1[posicion3] una el elemento 3(que es otro arreglo) y digo que subindice le tomo[0]

print (elemEnLista1)

rebanadaLista1 = lista1[0:3] #muestra una rebanada de la lista , toma hasta la posicion 3 pero no la muestra
print (rebanadaLista1)

#metodos

# print (dir(list)) #muestra los comandos que se puede hacer a la listas
num1= 12
lista4.append("prueba append")
lista1.append("prueba append2")

print (lista4)
print (lista1)

lista1.insert(1,"prueba insert") # inserta y desplaza a los demas elementos siguientes 
print(lista1)

lista1[1]= "prueba de reasignacion de datos" #reemplazas un elementos por otro en determinada posicion
print(lista1)

lista1.insert(3,num1)
print(lista1)

#eliminar elementos

precios = [100,300, 400, 100]

precios.pop() #elimina el ultimo elementos

print(precios)
precios.pop(1)
print(precios)

#precios.pop(5) # da error porque no hay 5 elemanos
#print(precios)


#como saber cuantos elementos hay en una lista

print(len(precios))
precios.pop( len(precios) -1) 
print (precios)

lista1.clear() # elimina todos los elementos de una lista
print (lista1)

precios.reverse() #vuelve para atras
print (precios)

#operador in

dniAlumnos =[40758687, 387648264, 8723648726]

if 40758687 in dniAlumnos:
    print("el alumno forma parte del curso")

else:
    print("el dni no existe")

# tuplas son listas inmutables, no se pueden cambiar como las listas y va entre ()

tupla1 =()
tupla2 =tuple()
tupla3 = 1,2,True
tupla4=(1,2,True)
tupla5=1-4 ,
tupla6=(True,)

print (tupla1)
print (tupla2)
print (tupla3)
print (tupla4)
print (tupla5)
print (tupla6)

tuplaConvLista=list(tupla4) #convierte una tupla en una lista
print(tuplaConvLista)

tuplaConvLista.append("soy un nuevo elemento")
print(tuplaConvLista)
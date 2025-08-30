lista=["jose","miguel","luis","pedro","pablo","ivan","juan"]
print (lista [5])
print(lista[0:4])

for i in lista:
    print(i)

lista2= lista
print(lista2)

lista2= lista[2:4]
print(lista2)

lista2= lista[:]
print(lista2)

lista2= lista[::-1]
print(lista2)


lista2= lista[-3]
print(lista2)

lista2=[1,2,5,7,9,8,10,12,15,20,30]
lista[6]="pepe"
print(lista)

lista.insert(6,"natalia")

lista.append("pedro pablo")
print(lista)


lista.extend(["jose","carlota","karen"])
print(lista)

lista.remove("pedro")
print(lista)

lista.pop(3)
print(lista)




for i in range (len (lista)):
    print(i,":",lista [i])

lista3="jose" in lista
print(lista3)

lista3="perensejo" in lista
print(lista3)


lista4=["a","a","b","b","c","c","a"]
cantidad=lista4.count("b")
print(cantidad)

lista.sort()
print(lista)

lista2.sort()
print(lista2)

lista6=sorted(lista)
print(lista6)


lista.reverse()
print(lista)

lista6=lista.copy()
print(lista6)
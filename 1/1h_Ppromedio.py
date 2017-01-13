nombre = raw_input("Primer usuario")
edad = raw_input("Edad")
edadN = int(edad)

nombre1 = raw_input("Segundo usuario")
edad1 = raw_input("Edad")
edadN1 = int(edad1)

nombre2 = raw_input("Segundo usuario")
edad2 = raw_input("Edad")
edadN2 = int(edad2)

print("Nombre \t\t Edad")
print(nombre+"\t\t"+edad)
print(nombre1+"\t\t"+edad1)
print(nombre2+"\t\t"+edad2)

suma = edadN+edadN1+edadN2
promedio  = suma/3
print("El prmedio de las edades es %d" %promedio)
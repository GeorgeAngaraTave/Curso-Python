# Agenda telefonica
# Jorge Angarita
# v0.1

def Bienvenidos():
    print("Bienbenido Agenda Telefonica")
    print("Selecciona una opcion: ")
    print("1- Ingresar un aregistro a la agenda")
    print("2- Listar el contenido de la angenda")

opcion = raw_input(" >")

if opcion == '1':
    print("Ingresar un aregistro a la agenda")
    nombre = raw_input("introduce Nombre")
    telefono = raw_input("introduce telefono")
    posiicon = raw_input("posicion en la lista")
    print("Se guardo la informacion Nombre", nombre, " Telefono", telefono)
    agendaCSV = open("Documentos/AngendaTelefonica1.csv", 'a')
    agendaCSV.write(posiicon)
    agendaCSV.write(";")
    agendaCSV.write("nombre: ")
    agendaCSV.write(";")
    agendaCSV.write(nombre)
    agendaCSV.write(";")
    agendaCSV.write(" Telefono:  ")
    agendaCSV.write(";")
    agendaCSV.write(telefono)
    agendaCSV.write(',\n')
  # agendaCSV = open("Documentos/AngendaTelefonica.csv")
   # print(agendaCSV.read())
   # agendaCSV.close()
elif opcion == '2':
    print(" Listar el contenido de la angenda")
    agendaCSV = open("Documentos/AngendaTelefonica1.csv")
    listaA = agendaCSV.readlines();
    for li in listaA:
        print li.replace(";","\t\t")
    #nemero = 0
    #while nemero < 25:
    #    print agendaCSV.readline()
    #    nemero = nemero + 1
    agendaCSV.close()
else:
    print(" La opcion no es valida")
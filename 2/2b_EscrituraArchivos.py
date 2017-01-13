#EL tipo w solo es para escribir pero orra los registros anteriores
agenda = open("Documentos/AgendaTelefonoca.txt",'a')
agendaCSV = open("Documentos/AngendaTelefonica.csv",'a')



##print(agenda.read())

#Borra el contenico
#agenda.truncate()
#agendaCSV.truncate()

nombre = raw_input("introduce Nombre")
telefono = raw_input("introduce telefono")

print("Se guardo la informacion Nombre",nombre," Telefono",telefono)

agenda.write("nombre: ")
agenda.write(nombre)
agenda.write(" Telefono:  ")
agenda.write(telefono+'\n')

agendaCSV.write("nombre: ")
agendaCSV.write(",")
agendaCSV.write(nombre)
agendaCSV.write(",")
agendaCSV.write(" Telefono:  ")
agendaCSV.write(",")
agendaCSV.write(telefono)
agendaCSV.write(',\n')
agenda = open("Documentos/AgendaTelefonoca.txt")
agendaCSV = open("Documentos/AngendaTelefonica.csv")
print(agenda.read())
print(agendaCSV.read())
agenda.close()
agendaCSV.close()

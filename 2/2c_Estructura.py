agendaCSV = open("Documentos/AngendaTelefonica1.csv")
agendaCSV1 = open("Documentos/AngendaTelefonica.csv", "r")
#print(agenda.read())

#print(agendaCSV.readline())

## Bucle FOR
#lineas=agendaCSV1.readlines()
#for li in lineas:
#    print li

#for i in range(0,3):
#    print agendaCSV.readline()

### WHILE
nemero = 0

while nemero <25:
    print agendaCSV.readline()
    nemero = nemero + 1



agendaCSV.close()



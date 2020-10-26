from Controller.personaController import personaController

lista=["María","Flores","99741236","F","0014",2]
enlace=personaController()
enlace.crearRegistro(lista)
listaRegistros=enlace.listarRegistros()
for i in range(len(listaRegistros)):
    print("Cód: ",listaRegistros[i][0])
    print("Nombre: ",listaRegistros[i][1])
    print("Apellido: ",listaRegistros[i][2])
    print("DNI: ",listaRegistros[i][3])
    print("Sexo: ",listaRegistros[i][4])
    print("Ciclo: ",listaRegistros[i][5])
    print("*************")
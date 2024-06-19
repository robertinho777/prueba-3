#https://github.com/robertinho777/prueba-3

import csv
lista = []
def val_pun ():
     valido = False
     while puntos > 150:
         print("puntuacion invalida, ingrese una puntuacion menor a 150: ")
         return

def act_nom ():
    op=input("seguro de que quiere cambiar el nombre del equipo?: (si / no)")
    if op == "si":
        return 1
    elif op == "no":
        return 0
    else:
        print("ingrese opcion valida.")

    
def estadisticas():
    cont = 0
    acum = 0
    punto = 0
    for x in lista:
        cont = cont+1
        acum = (acum+x[2])
    prom=acum/cont
    print("el promedio de puntos del equipo es de: ",prom)
    for x in lista:
        p = x[2]
        if punto<p:
            punto=x[2]
    print("la mayor cantidad de puntos fue de: ",punto)
        
while True:
    print("1. agregar equipo")
    print("2. listar equipo")
    print("3. actualizar nombre del equipo por id")
    print("4. generar base de datos")
    print("5. cargar base de datos")
    print("6. estadísticas")
    print("0. salir")

    op = int(input("ingrese una opcion: \n"))
    if op == 1:
        numero = int(input("ingrese numero del equipo: "))
        nombre = input("ingrese nombre del equipo: ")
        puntos = int(input("ingrese puntos del equipo: "))
        val_pun()
        if puntos < 40:
            categoria = "amateur"
        elif puntos >= 41 and puntos <= 80:
            categoria = "principiante"
        elif puntos >= 81 and puntos <= 120:
            categoria = "avanzado"
        elif puntos > 120 and puntos <= 150:
            categoria = "idolo"
         
        listaequipos=[numero,nombre,puntos,categoria]
        lista.append(listaequipos)
        
    elif op == 2:
        for x in lista:
            print("numero de equipo:", x[0],
                  "nombre del equipo:", x[1],
                  "puntos del equipo:", x[2],
                  "categoria del equipo: ",x[3])
    elif op == 3:
        encontrado = False
        act_nom()
        opcion=act_nom()
        if opcion==1:
            nombre = input("ingrese el nombre que desea cambiar: ")
            for x in lista:
                if nombre == x[1]:
                    print("numero de equipo:",x[0],
                      "nombre del equipo:",x[1],
                      "puntos del equipo:",x[2],
                        "categoria del equipo: ",x[3])
                    nuevo_nombre=input("ingrese el nombre nuevo: ")
                    listaequipos[1]=nuevo_nombre
                    print("nombre actualizado correctamente.")
                    encontrado = True
                    break
            if encontrado == False:
                print("el nombre de equipo dado no existe...")
        if opcion==0:
            print("nombre no actualizado")
    elif op == 4:
        print("generado base de datos...")
        with open('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
            escritor_csv = csv.writer(bbdd_equipos)
            escritor_csv.writerow(['num','nombre','puntos','categoria'])
            escritor_csv.writerows(lista)
            print("archivo generado exitosamente.")

    elif op == 5:
        with open('bbdd_equipos.csv','r',newline='')as bbdd_equipos:
            lector_csv = csv.reader(bbdd_equipos)
            for x in lector_csv:
                lista.append(x)
            print("archivo cargado con exito.")

    elif op == 6:
        estadisticas()

    elif op == 0:
        print("adios")
        break
    else:
        print("ingrese opcion valida")
        
    
                    
                   
    
                  
        
    

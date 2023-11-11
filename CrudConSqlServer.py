#Se importan las librerias a utilizar

#Estas librerias son meramente estéticas, el programa puede funcionar sin ellas
import os #os es el modulo que permite limpiar la pantalla
import msvcrt #msvcrt es el modulo que permite p
import pyodbc #Libreria utilizada para concentar con SQL
import pandas as pd

#Conexion a SQL server

server='JuanMedina'#El nombre del servidor
bd='Escuela'#El nombre de la base de datos
#Aqui se creo un usuario para acceder a SQL server, asi mismo el usuario se crea desde SQL
user='Usuario' #Usuario creado
password='admin'#Contraseña creado

#La conexion puede llegar a fallar, por eso se le complementa con un try
try:
    #Codigo que funge como conector, en el mismo se llama a un "driver"
    conector = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+ password)
    #print("Conexion exitosa")#Mensaje a desplegar si la conexion fue exitosa
except:
    print("La conexion ha fallado")#Mensaje a desplegar si la conexion no fue exitosa    

opc1=0#Opc1 que determinará si el usuario desea agregar otro valor
opc=0#Opc que determinará a que opción desea ir el usuario
a=True#a es la que nos indicara si el bucle principal(el del menú) continua
cursor3=conector.cursor()
cursor3.execute("Select * from Alumnos")
Alumnos= cursor3.fetchall()#Almacenara todos los valores de la bd
#Aqui se separaron las opciones por funciones 

#Función consultar datos
def Consultar():
    os.system ("cls")#Limpia la consola 
    print("1-.Consultar datos") 
    print("----------------")
    print("Datos almacenados:")
   #Forma 2 de ver datos
    cursor2=conector.cursor()
    cursor2.execute("Select * from Alumnos")
    Alumno= cursor2.fetchall()#Almacenara todos los valores de la bd
#Un bucle sencillo, que se encargara de desplegar los valores
    for y in Alumno:
     print(y)#Se imprime el valor#Se imprime el arreglo con los datos
    print("Presione una tecla para continuar...")
    msvcrt.getch()#"Pausa" el programa hasta que presiones alguna tecla
    cursor2.close()

#Función agregar datos
def Agregar(opc1):
    cursorI=conector.cursor()#Se crea un cursor con la función de insertar
    b=True #Mientras "b" sea True el ciclo se repetirá(se seguira pidiendo datos)
    while opc1!=1:#Mientras "opc1" sea diferente a 1, el ciclo se repetira
        try:#Try por si sucede alguna exception, evitando que el programa se cierre
            while b==True:#Si el bucle continua en true, se seguira corriendo
                os.system ("cls")#Limpia la consola  
                print("2-.Agregar datos")
                print("----------------")
                #Aqui se piden los datos a ingresar 
                nombre=input("Ingrese el nombre del alumno: ")
                apellido=input("Ingrese el apellido del alumno: ")
                edad=int(input("Ingrese la edad del alumno: "))

                #Comando para insertar
                insert="Insert into Alumnos (Nombre, Apellido, Edad) values (?,?,?);"#Los "?" sirven para explicarle al comando, que hay 3 datos que se implementaran despues
                cursorI.execute(insert,''+nombre+'',''+apellido+'',+edad)#Se junta el cursos con la ejecución

                #Esta parte es crucial, pues determinara si el ciclo continua
                opc1=int(input("¿Desea ingreasar otro alumno? [1=no][2=si]: "))
                if opc1==1:
                    b=False#Aqui se acaba el ciclo(El segundo, o sea agregar más valores), "b" es False
                os.system ("cls") 
        except ValueError as e: #Una exception, por si el usario ingresa valores inválidos
            print("Ingrese un valor válido")
            msvcrt.getch()
            os.system ("cls")   #Limpia la consola 
    cursorI.commit()#Commit "confirma" la modificación de los datos modificados
    cursorI.close()         

#Función "Modificar" datos            
def Modificar():
    cursorM=conector.cursor()#Se crea un cursor con la función de modificar
    os.system ("cls") #Limpia la consola 
    print("3-.Modificar datos")
    print("----------------")
    #Aqui solicita el dato a elminar(mediante su índice)
    x=int(input("Ingrese el índice del dato a modificar: "))
    #Aquí se "modifica"(realmente se está agregando un valor jajajaj XD)
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    edad=int(input("Ingrese la edad del alumno: "))
    #Todos los elemento a modificar requiere de un query diferente
    modificar1="UPDATE Alumnos set Nombre =? where id=?;"#Los "?" sirven para explicarle al comando, que hay datos que se implementaran despues
    modificar2="UPDATE Alumnos set Apellido =? where id=?;"
    modificar3="UPDATE Alumnos set Edad =? where id=?;"
    cursorM.execute(modificar1,''+nombre+'',x)#Se junta el cursos con la ejecución
    cursorM.execute(modificar2,''+apellido+'',x)
    cursorM.execute(modificar3,edad,x)
    print("Registro modificado")
    msvcrt.getch()  
    cursorM.commit()
    cursorM.close()

#Función eliminar
def Eliminar():
    cursorE=conector.cursor()#Se crea un cursor con la función de eliminar
    os.system ("cls") #Limpia la consola 
    print("4-.Eliminar datos")
    print("----------------")
    #Aqui se pregunta si se desea eliminar por índice o TODO
    print("1-.Eliminar por índice") 
    print("2-.Eliminar TODO")
    print("----------------")
    i=int(input("Ingrese una opción: "))#Pregunta por la opción
    if 1 ==i:
        os.system ("cls") #Limpia la consola 
        #Pregunta por el índice del dato a eliminar
        x=int(input("Ingrese el índice del dato a eliminar: "))
        #Eliminando datos
        eliminar="DELETE FROM Alumnos where id=?"
        cursorE.execute(eliminar,x)
        print("Registro eliminado")
        msvcrt.getch()  
    elif 2 ==i:
        os.system ("cls") #Limpia la consola 
        eliminar2="DELETE FROM Alumnos" 
        cursorE.execute(eliminar2)
        print("Todos los datos han sido eliminados") 
        msvcrt.getch()   
    else: #En caso de que el usuario no haya elegido una opción válida
        print("Ingrese una opción válida")         
        print("Presione una tecla para continuar...")
        msvcrt.getch()      
    cursorE.commit()
    cursorE.close()

#"Main" del programa
while True: #El bucle, que determinará a hacía dónde se movera el usuario, ademas de finalizar el programa
    try:#En caso de que el usuario no selecciona una opcion válida, o ingrese un valor no admitible
        while a ==True:#Mientras "a" sea True el ciclo se repetira, y se podrá navegar indefinidamente 
            print("Proyecto Crud")
            print("----------------")
            print("1-.Consultar datos")
            print("2-.Agregar datos")
            print("3-.Modificar datos")
            print("4-.Eliminar datos")
            print("5-.Salir")
            print("----------------")
            opc=int(input("Seleccione una opción: "))#Aqui se tomará el valor para "navegar" por los menús

            if opc== 1:
                Consultar()
            elif opc== 2:                           
                Agregar(opc1)
                opc1=0     
            elif opc==3:
                tamaño=len(Alumnos)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función modificar
                    print("No existe un dato a modificar")
                    msvcrt.getch()    
                else:
                    Modificar()    
            elif opc==4:
                tamaño=len(Alumnos)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función eliminar
                    print("No existe un dato a eliminar")
                    msvcrt.getch()    
                else:
                    Eliminar()
            elif opc==5:
                os.system ("cls") 
                print("Saliste")
                print("----------------") 
                print("Presione una tecla para continuar...")
                msvcrt.getch()     
                a=False  #Al salir el bucle finaliza, y por ende el programa también 
            else:
                os.system ("cls") 
                print("Escribe una opción válida")  #En caso de que el usuario no haya ingresado una opción válida
                msvcrt.getch()          
    except ValueError as e: #Por si el usuario ingreso un valor INVALIDO(Un string por ejemplo)
        print("Selecciona una opción valida")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        os.system ("cls")   
    else: 
        break #Se termina el programa
   
#Siempre al terminar el programa, se deben cerrar las conexiones
cursor3.close()
conector.close()
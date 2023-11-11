#Se importan las librerias a utilizar

#Estas librerias son meramente estéticas, el programa puede funcionar sin ellas
from distutils.command.clean import clean
import os #os es el modulo que permite limpiar la pantalla
import msvcrt #msvcrt es el modulo que permite p

Alumnos=[]#Se crea la matriz que almacenará los valores
opc1=0#Opc1 que determinará si el usuario desea agregar otro valor
opc=0#Opc que determinará a que opción desea ir el usuario
a=True#a es la que nos indicara si el bucle principal(el del menú) continua

#Aqui se separaron las opciones por funciones 

#Función consultar datos
def Consultar():
    os.system ("cls")#Limpia la consola 
    print("1-.Consultar datos") 
    print("----------------")
    print("Datos almacenados:")
    print(Alumnos)#Se imprime el arreglo con los datos
    print("Presione una tecla para continuar...")
    msvcrt.getch()#"Pausa" el programa hasta que presiones alguna tecla

#Función agregar datos
def Agregar(opc1):
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
                #Los datos ingresandos se "empaquetan" en una tupla
                alumno=(nombre,apellido,edad)
                #Los datos almacenados en la tupla se agregan al arreglo
                Alumnos.append(alumno)
                #Esta parte es crucial, pues determinara si el ciclo continua
                opc1=int(input("¿Desea ingreasar otro alumno? [1=no][2=si]: "))
                if opc1==1:
                    b=False#Aqui se acaba el ciclo(El segundo, o sea agregar más valores), "b" es False
                os.system ("cls") 
        except ValueError as e: #Una exception, por si el usario ingresa valores inválidos
            print("Ingrese un valor válido")
            msvcrt.getch()
            os.system ("cls")   #Limpia la consola  

#Función "Modificar" datos            
def Modificar():
    os.system ("cls") #Limpia la consola 
    print("3-.Modificar datos")
    print("----------------")
    #Aqui solicita el dato a elminar(mediante su índice)
    x=int(input("Ingrese el índice del dato a modificar: "))
    #Aquí se "modifica"(realmente se está agregando un valor jajajaj XD)
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    edad=int(input("Ingrese la edad del alumno: "))
    #Mismo proceso, los datos ingresados se empaquetan en un dupla
    alumno=(nombre,apellido,edad)
    #Los datos se agregan al arreglo
    Alumnos.insert(x,alumno)
    #Aqui se elimina el dato que se "modifico"
    Alumnos.pop(x+1)#Es importante el"x+1", ya que es el indice del valor a "modificar", el dato se termina borrando
    print("Registro modificado")
    msvcrt.getch()  

#Función eliminar
def Eliminar():
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
        #Cache realmente no sirve para nada, es un elemento "visual", que mostrara el valor eliminado
        cache=Alumnos[x]
        #Aqui el valor se eliminó, "x" fue la posición del valor
        Alumnos.pop(x)
        print(f"Registro {cache} eliminado")#Aqui empleamos cache, para un uso visual
        msvcrt.getch()  
    elif 2 ==i:
        os.system ("cls") #Limpia la consola 
        Alumnos.clear()#Aqui se borraron TODOS los datos
        print("Todos los datos han sido eliminados") 
        msvcrt.getch()   
    else: #En caso de que el usuario no haya elegido una opción válida
        print("Ingrese una opción válida")         
        print("Presione una tecla para continuar...")
        msvcrt.getch()      

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
   

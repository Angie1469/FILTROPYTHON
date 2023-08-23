import os
import json            


def leerJson():
    with open("manual.json","r") as file:
        data = json.load(file)
    return data

def escribirJson(data):
    with open("manual.json","w") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)


def validarFloat(numero):
    while True:
        try:
            n = float(input(numero))
            return n
        except ValueError:
            print("Error. Número real inválido. intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
        except Exception as e:
            print("Ha sucedido un Error: ", e)
        
   

def validarString(nombre):
    while True:
        try:
            n = input(nombre)
            if n == None or n.strip() == "":
                print("Nombre inválido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            
   

def validarEntero(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            r = 5 /n
            return n
        except ValueError:
            print("Error. Número entero inválido. intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
        except ZeroDivisionError:
            print("Error. No se puede dividir por cero.")
            input("Presione cualquier tecla para continuar...")

def validarOtroCiclo(msg):
    while True:
        try:
            a=input(msg)
            if a.lower() == "si":
                return True
            if a.lower() == "no":
                return False
            print("input error")
        except ValueError:
            print("input error")
            continue




def Crear():
    data = leerJson()
    temas = []
    op = validarString("Que desea crear un manual o un tema? ")
    if op == "manual":
        lenguaje = validarString("Ingrese el nombre del lenguaje:")
        autor = validarString("Ingrese el nombre del autor:")
        paginas = validarString("Ingrese la cantidad de paginas")

        data["manuales"][lenguaje] = {
            "autor": autor,
            "paginas": paginas,
        }
    else: 
        op == "tema"
        lenguaje = validarString("a que lenguaje desea agregar el tema:")
        titulo = validarString("Ingrese el titulo:")
        clasificacion = validarEntero("Ingrese la clasificacion (1-2-3):")
        data["manuales"][lenguaje]["temas"].append({ 
            "Titulo": titulo,
            "Clasificación": clasificacion,
        })

    
    print(data)
    escribirJson(data)
    


def Modificar():
   pass

def Eliminar():
    data = leerJson()
    eliminar = validarString("Desea eliminar un manual o un tema?")
    if eliminar == "manual":
        manual = validarString("Que manual desea eliminar?")
        del data["manuales"][manual]
        print("El manual ha sido eliminado satisfactoriamente")
    else:
        tema = validarEntero("Cual tema desea eliminar?")
        for i in data["manuales"]:
            for j in ["temas"]:
                data["manuales"]["temas"].remove(tema)
    escribirJson(data)

def Listar():
    for n in Data['manuales']:
        print (Data)
        

def GenerarInformeDatos():
    data = leerJson
    resultado = ""
    for lenguaje in data["manuales"].keys():
        c1=0
        c2=0
        c3=0
        resultado += f"Manual  {lenguaje}: \n"
        if "temas" in data["manuales"][lenguaje]:
            for tema in data["manuales"][lenguaje]["temas"]:
                if tema["clasificación"]==1:
                    c1+=1
                if tema ["clasificación"]==2:
                    c2+=1
                if tema ["clasificación"]==3:
                    c3+=1
        resultado += f"Temas basicos: {c1}***Temas intermedios: {c2}*** Temas avanzados: {c3}***"
    with open("datos.txt","w", encoding="utf-8") as file:
        file.write(resultado)


def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee")
        print(" "*6 + "1) Crear")
        print(" "*6 + "2) Modificar")
        print(" "*6 + "3) Eliminar")
        print(" "*6 + "4) Listar")  #****
        print(" "*6 + "5) Generar Informe Datos\n")  #****
        print(" "*6 + "6) Salir del programa") 
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
       
        switch = { 1: Crear, 2: Modificar, 3: Eliminar, 
                  4: Listar, 5: GenerarInformeDatos}
        switch[opcion]()


Data = {}
Data = leerJson()
menu()
escribirJson(Data)

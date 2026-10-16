import os
nombre_mascota=[""]*3
edad_mascota=[0]*3

def insertar():
    for i in range(len(nombre_mascota)):
        nombre_mascota[i]= input(f"Ingrese nombre mascota: ")
        edad_mascota[i]=int(input(f"Ingrese edad mascota: "))

def mostrar():
    for i in range(len(nombre_mascota)):
        print(f"Nombre: {nombre_mascota[i]}, edad: {edad_mascota[i]}")

def eliminar(nombreborrar):
    for i in range(len(nombre_mascota)):
        if nombre_mascota[i] == nombreborrar:
            for j in range(i,len(nombre_mascota)-1):
                nombre_mascota[j] = nombre_mascota[j+1]
                edad_mascota[j] = edad_mascota[j+1]
                nombre_mascota[-1] = ""
                edad_mascota[-1] = 0
                print(f"Mascota eliminada {nombre_mascota[i]}")
                return    

def ordenar():
    for i in range(len(nombre_mascota)):
        for j in range(len(nombre_mascota)-1):
            mascota1 = nombre_mascota[j]
            mascota2 = nombre_mascota[j+1]
            if mascota1[0] > mascota2[0]:
                temporal = nombre_mascota[j]
                nombre_mascota[j] = nombre_mascota [j+1]
                nombre_mascota[j+1] = temporal
    print("Mascota ordenadas")

def main():
    global nombre_mascota, edad_mascota
    nombre_mascota=[""]*3
    edad_mascota=[0]*3
    opcion = 0
    while opcion != 4:
        os.system ('cls'if os.name =='nt'else'clear')
        print ("===============REGISTRO DE MASCOTAS===============")
        print ("1. Insertar mascota (nombre | edad)")
        print ("2. Mostrar mascotas (nombre | edad)")
        print ("3. Eliminar mascotas por nombre (en ambos vectores)")
        print ("4. Odernar mascota alfabeticamente")
        print ("5. Salir")
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            insertar()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            mascotaborrar = input("Ingrese mascota a borrar: ")
            eliminar(mascotaborrar)
        elif opcion ==4:
            ordenar()
            mostrar()
        elif opcion == 5:
            print("Saliendo...")
        else: print ("Opción inválida")
        if  opcion !=4:input("Presiones para continuar ")
main()

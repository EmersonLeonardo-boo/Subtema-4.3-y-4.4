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
        print ("4. Salir")
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            insertar()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
                print("Eliminar")
        elif opcion == 4:
                print("Saliendo...")
        else: print ("Opción inválida")
        if  opcion !=4:input("Presiones para continuar ")
main()

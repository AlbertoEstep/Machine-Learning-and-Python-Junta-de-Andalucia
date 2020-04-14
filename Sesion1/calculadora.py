#Author: Alberto Estepa Fernandez
#Date: 15-04-2020


diccionario_opciones = {1 : 'agregar', 2 : 'restar', 3 : 'multiplicar',
                        4 : 'dividir', 5 : 'salir del programa'}


def bienvenida():
    print("\t-----------------------------------------------------------------\t\n")
    print("\t|  Bienvenido, pulse \'Enter\' para ver las opciones disponibles  |\t\n")
    print("\t-----------------------------------------------------------------\t\n")
    input();

def imprimir_opciones():
    print("\tOpciones:\n")
    print("\t\tPulse 1 para Agregar\n")
    print("\t\tPulse 2 para Restar\n")
    print("\t\tPulse 3 para Multiplicar\n")
    print("\t\tPulse 4 para Dividir\n")
    print("\t\tPulse 5 para Salir del programa\n\n")

def pedir_accion():
    while True:
        opcion = input("\t\tElige una opcion (numero de 1 a 5): ")
        try:
            opcion = int(opcion)
            if (opcion < 6 and opcion > 0):
                return opcion
            else:
                print("\t\tATENCIÓN: Debe ingresar un número entero entre 1 y 5.")
        except ValueError:
                print("\t\tATENCIÓN: Debe ingresar un número entero entre 1 y 5.")

def pedir_numero():
    while True:
        numero = input("\t\tIntroduce un numero: ")
        try:
            float(numero)
            return numero
        except ValueError:
            print("\t\tATENCIÓN: Debe ingresar un valor numérico")


def efectuar_accion(opcion):
    print("\n\t\tHas elegido la opcion '" + diccionario_opciones[opcion] + "'");
    if(opcion == 1):
        numero1 = pedir_numero()
        numero2 = pedir_numero()
        print("\n\t\tEl resultado de {} los números {} y {} es {}\n".format(
            diccionario_opciones[opcion], numero1, numero2, float(numero1) +
            float(numero2)))
    elif(opcion == 2):
        numero1 = pedir_numero()
        numero2 = pedir_numero()
        print("\n\t\tEl resultado de {} los números {} y {} es {}\n".format(
            diccionario_opciones[opcion], numero1, numero2, float(numero1) -
            float(numero2)))
    elif(opcion == 3):
        numero1 = pedir_numero()
        numero2 = pedir_numero()
        print("\n\t\tEl resultado de {} los números {} y {} es {}\n".format(
            diccionario_opciones[opcion], numero1, numero2, float(numero1) *
            float(numero2)))
    elif(opcion == 4):
        numero1 = pedir_numero()
        numero2 = pedir_numero()
        while(numero2 == str(0)):
            print("\t\tLe recordamos que no puede dividir por cero.")
            numero2 = pedir_numero()
        print("\n\t\tEl resultado de {} los números {} y {} es {}\n".format(
            diccionario_opciones[opcion], numero1, numero2, float(numero1) /
            float(numero2)))
    else:
        print("\n\t\tHasta luego!\n")

def main():
    bienvenida()
    imprimir_opciones()
    opcion = pedir_accion()
    efectuar_accion(opcion)

if __name__ == "__main__":
    main()

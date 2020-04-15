#Author: Alberto Estepa Fernández
#Date: 15-04-2020


################################################################################
###########                                                     ################
###########         Funciones y variables auxiliares            ################
###########                                                     ################

# Sumar dos numeros (se entiende que los parámetros son strings)
def sumar(numero1, numero2):
    return float(numero1) + float(numero2)

# Restar dos numeros (se entiende que los parámetros son strings)
def restar(numero1, numero2):
    return float(numero1) - float(numero2)

# Multiplicar dos numeros (se entiende que los parámetros son strings)
def multiplicar(numero1, numero2):
    return float(numero1) * float(numero2)

# Dividir dos numeros (se entiende que los parámetros son strings)
# Requisito: el denominador no sea igual a cero
def dividir(numero1, numero2):
    return float(numero1) / float(numero2)

# Pedir un número al usuario
def pedir_numero():
    while True:
        numero = input("\t\tIntroduce un numero: ")
        try:
            float(numero)
            return numero
        except ValueError:
            print("\t\tATENCIÓN: Debe ingresar un valor numérico")

diccionario_opciones = {1: 'agregar', 2: 'restar', 3: 'multiplicar',
                        4: 'dividir', 5: 'salir del programa'}

diccionario_funcion = {1: sumar, 2: restar, 3: multiplicar, 4: dividir}

###########                                                     ################
################################################################################


################################################################################
###########                                                     ################
###########                 Funciones del programa              ################
###########                                                     ################

# Mensaje de bienvenida
def bienvenida():
    print("\t-----------------------------------------------------------------\t\n")
    print("\t|  Bienvenido, pulse \'Enter\' para ver las opciones disponibles  |\t\n")
    print("\t-----------------------------------------------------------------\t\n")
    input();

# Imprimimos las opciones disponibles para el usuario
def imprimir_opciones():
    print("\tOpciones:\n")
    print("\t\tPulse 1 para Agregar\n")
    print("\t\tPulse 2 para Restar\n")
    print("\t\tPulse 3 para Multiplicar\n")
    print("\t\tPulse 4 para Dividir\n")
    print("\t\tPulse 5 para Salir del programa\n\n")

# Pedir el codigo de una accion al usuario
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

# Efectuamos la acción
def efectuar_accion(opcion):
    print("\n\t\tHas elegido la opcion '" + diccionario_opciones[opcion] + "'");
    if(opcion != 5):
        numero1 = pedir_numero()
        numero2 = pedir_numero()
        if(opcion == 4):
            while(numero2 == str(0)):
                print("\t\tLe recordamos que no puede dividir por cero.")
                numero2 = pedir_numero()
        fun = diccionario_funcion[opcion]
        print("\n\t\tEl resultado de {} los números {} y {} es {}\n".format(
            diccionario_opciones[opcion], numero1, numero2, fun(numero1, numero2)))
    else:
        print("\n\t\tHasta luego!\n")

###########                                                     ################
################################################################################

################################################################################
###########                                                     ################
###########                 Funcion principal                   ################
###########                                                     ################

# Función principal del programa
def main():
    # Mensaje de bienvenida
    bienvenida()
    # Imprimimos las opciones disponibles para el usuario
    imprimir_opciones()
    # Captamos la acción solicitada
    opcion = pedir_accion()
    # Efectuamos la acción
    efectuar_accion(opcion)

###########                                                     ################
################################################################################

if __name__ == "__main__":
    main()

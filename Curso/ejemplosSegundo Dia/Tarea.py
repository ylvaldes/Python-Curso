def h2tx():
    print("Introduce una hora en el formato hh:mm.")
    hora = 10
    return hora
def f2tex(fecha):
    print("Introduce una fecha en el formato dd/mm/yyyy.")
    return fecha
def sumaH(hora1,hora2):
    print("Introduce dos hora en el formato hh:mm separadas por espacio.")
    return hora1+hora2
def imprimeMenu():
    print("********************************************************")
    print("*                   OPERACIONES                        *")
    print("* 1- Hora a Texto                                      *")
    print("* 2- Fecha a Texto                                     *")
    print("* 3- Sumar Horas                                       *")
    print("********************************************************")
def main():
    imprimeMenu()
    operacion={1:h2tx, 2:f2tex,3:sumaH}
    seleccion= input("Escriba la Operacion a ralizar: ")
    try:
        resultado= operacion[seleccion]
        print(resultado)
    except:
        print("intente de nuevo")
if __name__ == '__main__': main()
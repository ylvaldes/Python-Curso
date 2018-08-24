#!/usr/bin/env python3
def main():
    x=int(input('Maximum number: ')) # Solicita un string y con la funcion INT convierte a un ntero
    s=range(x) # Obtiene el rango hasta ese valor 
    a=[x*2 for x in s] #Se hace una lista de elementos del rango multiplicados por 2
    b=[x for x in s if x%3==0]  # Se hace una lista con los elemetos del rango multiplos de 3
    from math import pi   # Importo la libreria Math y de ella pi
    c=[round(pi,i)for i in s] #Crea una lista con los elementos de PI Redondeando el numero pi a tantos decimales que tenga I
    d={x:x**2 for x in s} #Crea un diccionario con sus numeros y sus cuadrados 
    e={x:x**2 for x in s if x not in b} #Crea un diccionario con sus numeros y sus cuadrados que no son divisibles por 3 
    print_list(s) # Imprime una lista
    print_list(a)
    print_list(b)
    print_list(c)
    print(d)   # Implime un diccionario
    print(e)
def print_list(o):
    for x in o:print(x,end = ' ')
    print()
if __name__ == '__main__': main()

#!/usr/bin/env python3
def main():
    a=set(input('Enter a word: '))  # Lee una cadena de caracteres y se convierte en un conjunto con set
    b=set(input('Enter another word: '))  # Lee una cadena de caracteres y se convierte en un conjunto con set
    print('a   = ',end='');print_set(a)  #
    print('b   = ',end='');print_set(b)
    print('a&b = ',end='');print_set(a&b) # Multiplica de forma logica a*b Los caracteres de a que coinciden en el b
    print('a|b = ',end='');print_set(a|b)  # Suma logica los caracteres de a mas los caracteres de b eliminando los repetidos 
    print('a^b = ',end='');print_set(a^b)  # Union exclusiva, los elementos que se repiten en ambos conjuntos no se pone 
def print_set(o):
    print('{',end='')
    for x in o:print(x,end='')
    print('}')
if __name__ == '__main__': main()


# set es un conjunto 
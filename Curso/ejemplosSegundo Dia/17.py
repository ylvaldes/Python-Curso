#!/usr/bin/env python3
def main():
    numbers={'one':'uno','two':'dos','three':'tres'} #se crea un diccionario de clave valor 
    print_dict(numbers)
def print_dict(o):
    for x in o:print('{}: {}'.format(x,o[x])) # Se obtiene el Key con la x y en o[x] se obtiene el valor del valor
if __name__=='__main__':main()

#!/usr/bin/env python3
def main():
    x=open('lines.txt','rt') # Abre el archivo en solo lectura
    y=open('lines-copy.txt','wt') # Modo escritura, al no existir se crea un nuevo fichero 
    for i in x:
        print(i.rstrip(),file=y) # Se copian los elementos del archivo x al y.
    y.close()
if __name__=='__main__':main()

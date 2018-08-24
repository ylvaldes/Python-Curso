#/usr/bin/env python3
def main():
    i=open('binary.dat','rb') #Se abre en modo lectura de un archivo del tipo Binario (rb)
    o=open('binary-copy.dat','wb')  #Se escribe un archivo del tipo Binario (wb)
    while True:
        b=i.read(100000000) # Lee de cada 100000 cantidad de byte del bufer del archivo  #read metodo para leer archivo binario
        if b:
            o.write(b)  # Metodo para escribir en un archivo binario
        else: 
            break
    o.close()
if __name__=='__main__':main()

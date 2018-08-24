#!/usr/bin/env python3
class Service: # Se crea una clase servicio
    lista=[1,2,3]  # Variable propia de la clase
    def __init__(self,**kwargs): # Inicializar los Objetos de las clases 
        self._type=kwargs['type'] if 'type' in kwargs else '"unknown service type"'
        self._app=kwargs['app'] if 'app' in kwargs else '"unknown app"'
        self._version=kwargs['version'] if 'version' in kwargs else '"unknown version"'
    def type(self,t=None):
        if t:self._type=t
        return self._type
    def app(self,a=None):
        if a:self._app=a
        return self._app
    def version(self,v=None):
        if v:self._version=v  #Setter
        return self._version  # Getter 
    def __str__(self): # Forma de imprimir un Objeto se define y automaticamente los print se retornan de esta forma 
        return 'The {} is {} ({})'.format(self.type(),self.app(),self.version()) # Se configura para que se devuelva el el objeto de esta forma
def main():
    x=Service(type='DNS',app='bind',version='9.11')
    y=Service(type='Web',app='nginx',version='1.13')
    z=Service(type='DB',app='mysql',version='5.5')
    for i in x,y,z:
        print(i)
    print(Service())
    z.version('5.6') # se modifica la variable propia del objeto 
    print(z)  #Se modifica el valor de la version modificada
    print(x)  
    print(z.lista)
    z.lista[0]=8  # La variable de la clase lista se puede modificar desde la propia clase. 
    print(z.lista)
    print(x.lista) 
if __name__ == '__main__': main()

    # Desde fuera de las clases nunca se deben modificar los _ solo en los Setter y Getter de la propia Clase
    # Los valores de los objetos se modifican con los Setter y getter de esos objetos 
    # Si se modifica una Variable gloval de la lista de modifican para todos los objetos creados
    # Obejtos especiales de Python _str_ 
    # Cuando se llama el objeto sin parametros actua como un Getter y cuando es con elementos actua como un Setter

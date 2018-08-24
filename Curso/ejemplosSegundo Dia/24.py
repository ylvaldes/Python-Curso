#!/usr/bin/env python3
class Service:
    def __init__(self,**kwargs): #Inicializo los Objetos de la clase con un diccionario
        if 'type' in kwargs:
            self._type=kwargs['type']
        if 'app' in kwargs:
            self._app=kwargs['app']
        if 'version' in kwargs:
            self._version=kwargs['version']
    def type(self,t=None):                                           # Los Setter Getter de la clase para Type (Si vienen parametro se modifica el valor si es false se retorna el valor y si no tiene se lanza el valor por defecto) 
        if t:
            self._type=t                    
        try:                                                          # Se agrega porque si no tiene valor pone un valor por defecto
            return self._type                                        # Al hacer el retorno no existe se lanza una excepcion que asigna por defecto un valor 
        except AttributeError:
            return '"unknown service type"'
    def app(self,a=None):                                            # Los Setter Getter de la clase para app
        if a:
            self._app=a
        try:
            return self._app
        except AttributeError:
            return '"unknown app"'
    def version(self,v=None):                                    # Los Setter Getter de la clase para version
        if v:
            self._version=v
        try:
            return self._version
        except AttributeError:
            return '"unknown version"'
    def __str__(self):                                               # Modifico la forma de hacer el Print
        return 'The {} is {} ({})'.format(self.type(),self.app(),self.version())

class DNS(Service):                                                 # Se crean subClases DNS de la Superclase Servicios
    def __init__(self,**kwargs):
        self._type='DNS'                                      #Crea un objeto del tipo de la clase en este caso DNS
        if 'type' in kwargs:                                  # Si pongo el valor del typo se borra y se deja el que se define en la subclase
            del kwargs['type']
        super().__init__(**kwargs)                             #Se llama a la superClase a la que pertenese y sustituye el objeto
class Web(Service):
    def __init__(self,**kwargs):
        self._type='Web'
        if 'type'in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)
class DB(Service):
    def __init__(self,**kwargs):
        self._type='DB'
        if'type'in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)
    def password(self,p=None):
        if p:
            self._password=p
        try:
            return self._password
        except AttributeError:
            return 'unknown.'
    def __str__(self):     # Se crea el metodo STR propio para la subclase BD adaptandolo a la particularidad de la Subclase
        return 'The {} is {} ({}) and the root password is: {}'.format(self.type(),self.app(),self.version(),self.password())
def main():
    x=DNS(app='bind',version='9.11')  # Se llama a la subclase directamente para crear los objetos 
    y=Web(app='nginx',version='1.13')
    z=DB(app='mysql',version='5.5')
    for i in x,y,z:
        print(i)
    print(Service())
    z.version('5.6')
    print(z)
    print(x)
    print(z)
    z.password('pa$$w0rd')
    print(z)
if __name__ == '__main__': main()


# En las clases hijas se pueden definir metodos propios o modificar los metodos de la clase padre a la sparticularidades de las hijas. 
#
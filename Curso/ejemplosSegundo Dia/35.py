#!/usr/bin/env python3
def n2w(nn):
    n=tuple(nn) #Convierto NN en una tupla 
    d=n[0]  # Almaceno el primer valor de la tupla a las decenas 
    u=n[1]  # Almaceno el segundo valor de la tupla a las decenas 
    ones=(None,'Una','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve')
    tens=(None,'Diez','Veinte','Treinta','Cuarenta','Cincuenta')
    teen=(None,'once','doce','trece','catorce','quince','diciseis','diecisiete','dieciocho','diecinueve')
    if d=='0':
        return ones[int(u)]
    elif u=='0':
        return tens[int(d)]
    elif d=='1':
        return teen[int(u)]
    else:
        return '{}-{}'.format(tens[int(d)],ones[int(u)])
class time2words:
    def __init__(self,time):  # Inicializa el objeto con la hora 
        _t=time.split(':')    # A la hora le hago un Split separado por : una tupla con horas y minutos
        self._hour=_t[0]   #Hora le asigno el 1 elemento de la tupla
        self._minute=_t[1] # minuto le asigno el segundo elemento de la tupla
    def hour(self):        # Getter horas
        return self._hour
    def minute(self):     # Getter minuto
        return self._minute
    def h2w(self):      # Convierte la hora de numero a texto
        _H=self.hour()
        _h=int(_H)
        if int(self.minute())<=30:
            if _h==0:
                return 'media noche'
            elif _h==12:
                return 'medio dia'
            else:
                return n2w(_H)
        else:
            if _h==23:
                return 'media noche'
            elif _h==11:
                return 'medio dia'
            elif _h<9:
                return n2w('0'+str(1+_h))
            else:
                return n2w(str(1+_h))
    def m2w(self):    # Minutoa de numero a palabras
        _M=self.minute()
        _m=int(_M)
        if _m==0:
            return "en punto"
        elif _m==30:
            return 'y media'
        elif _m==15:
            return 'y cuarto'
        elif _m<30:
            return '{} past'.format(n2w(_M))
        elif _m<51:
            return '{} to'.format(n2w(str(60-_m)))
        else:
            return '{} para el'.format(n2w('0'+str(60-_m)))
    def __str__(self):
        if self.minute()=='00':
            return '{} {}'.format(self.h2w(),self.m2w())
        else:
            return '{} {}'.format(self.m2w(),self.h2w())
def main():
    lista=('11:55','03:03','00:15','23:45','08:45','12:50','14:00','18:50','17:00')
    for x in lista:
        print('{} -> {}'.format(x,time2words(x)))
    seguir='SI'
    while seguir=='SI':
        n=int(input('Numero entre 1 y 999.999.999: '))
        while n>999999999:
            n=int(input('fuera de rango, intenta de nuevo: '))
        christian=main()
        print(' '.join(christian),'\n')
        seguir=input('Continuar < si - no >: ').upper()


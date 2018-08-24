#!/usr/bin/env python3
def n2w(nn):
    n=tuple(nn);d=n[0];u=n[1]
    ones=(None,'one','two','three','four','five','six','seven','eight','nine')
    tens=(None,'ten','twenty','thirty','forty','fifty')
    teen=(None,'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
    if d=='0':
        return ones[int(u)]
    elif u=='0':
        return tens[int(d)]
    elif d=='1':
        return teen[int(u)]
    else:
        return '{}-{}'.format(tens[int(d)],ones[int(u)])
class t2w:
    def __init__(self,time):
        _t=time.split(':');
        self._hour=_t[0];
        self._minute=_t[1]
    def hour(self):
        return self._hour
    def minute(self):
        return self._minute
    def h2w(self):
        _H=self.hour();
        _h=int(_H)
        if int(self.minute())<=30:
            if _h==0:
                return 'midnight'
            elif _h==12:
                return 'noon'
            else:
                return n2w(_H)
        else:
            if _h==23:
                return 'midnight'
            elif _h==11:
                return 'noon'
           # elif _h<9:
            #    return n2w('0'+str(1+_h))
            else:
                return n2w(str(1+_h))
    def m2w(self):
        _M=self.minute();_m=int(_M)
        if _m==0:
            return "o'clock"
        elif _m==30:
            return 'half past'
        elif _m==15:
            return 'quarter past'
        elif _m==45:
            return 'quarter to'
        elif _m<30:
            return '{} past'.format(n2w(_M))
        #elif _m<51:
         #   return '{} to'.format(n2w(str(60-_m)))
        else:
            return '{} to'.format(n2w(str(60-_m)))
    def __str__(self):
        if self.minute()=='00':
            return '{} {}'.format(self.h2w(),self.m2w())
        else:
            return '{} {}'.format(self.m2w(),self.h2w())


#Palabra self identifica a la variables y metodos de una misma clase
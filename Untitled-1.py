def fib(numero):
        """Calcula la serie Fibonachi de un numero entrado por parametros """
        a,b=0,1
        while numero<100:
                print(a,end=' ')
                a,b=b,a+b
        print()
        
areglo= []
a,b,c,d=0,1,10,5
while(b<10):
       areglo.append(b) 
       a,b=b,a+b
print(areglo) 
for a in areglo:
        if a<50:
                c=c*a
                print(a , ',', c)
        else:
                d=d*a
                print(a , ',', d)

print(areglo[:])
print(areglo.pop())


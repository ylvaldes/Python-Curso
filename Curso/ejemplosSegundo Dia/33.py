#!/usr/bin/env python3
x=(1,0,0,1,0)
print(x)
print(len(x))
print(list(reversed(x))) # La lista invertida de la tupla (se )
print(sum(x))
print(max(x))
print(min(x))
print(any(x))
print(all(x))
y=(0,1,1,1,0)
for a,b in zip(x,y):
    print('{} - {}'.format(a,b))
z=('red','green','blue')
for a,b in enumerate(z):
    print('{}: {}'.format(a,b))

# Trabajo con tuplas
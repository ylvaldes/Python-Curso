#!/usr/bin/env python3
clouded=input('Is it clouded?(y/n): ')
x='It might rain.'if clouded=='y' else 'It is sunny.'
print(x)
n=int(input('How many items are there in the box? '))
x='The box is not empty.'if n else 'It is empty.'
print(x)

# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:24:22 2021

@author: socha
"""
pobranalista=input("napisz liczby oddzielone przecinkami i nacisnij enter")
lista2=[]
for i in range (len(pobranalista)):
    lista2.append(int(pobranalista[i]))

print("pobrana lista:", pobranalista)
print("lista2:", lista2)

    
    
    
    
"""
lista=[]
print("lista:", lista)
lista.append(3)
print("lista:", lista)
lista.append(7)
print("lista:", lista)

zmienna=input("napisz liczbę i nacisnij enter")
print(zmienna)
#c=zmienna+"str"
c=int(zmienna)+4
print("zmienna c:", c)

    



def dodawanie(a,b):
    c=a+b
    return c

x=[2,5,7,1,0,2,6,9]
print("lista x:",x)
x2=(sorted(x))
print("lista x po wywyolaniu funkcji sorted",x)
print("lista x2:",x2)

pom=dodawanie(2,7)
pom=pom+1
print(pom)




def sortowanie(lista):
    n=len(lista)

    for i in range (0,n-1):
        for j in range (i+1,n):
            if lista[i]>lista[j]:
            
                lista[i],lista[j]=lista[j],lista[i]
                
            
x=[2,5,7,1,0,2,6,9]
print("lista x:",x)
sortowanie(x)
print("lista x po sortowaniu:",x)

y=[4,6,1,9,6]
print("lista y:",y)
sortowanie(y)
print("lista y po sortowaniu:",y)
"""

"""
"""
"""
lista=[2,5,7,1,0,2,6,9]
n=len(lista)
print(n)

for i in range (0,n-1):
    for j in range (i+1,n):
        if lista[i]>lista[j]:
            
            lista[i],lista[j]=lista[j],lista[i]
            
print(lista)
"""

"""
"""
"""
a=1
b=2

print("a=",a)
print("b=",b)


a,b=b,a

print("po zmianie")
print("a=",a)
print("b=",b)
"""
"""
"""
"""
lista=[2,5,7,1,0,2,6,9]
n=len(lista)
print(n)

for i in range (0,n-1):
    for j in range (i+1,n):
        if lista[i]>lista[j]:
            pom=lista[i]
            lista[i]=lista[j]
            lista[j]=pom
            
print(lista)



"""
"""
lista=[2,5,7,1,0,2,6,9]
n=len(lista)

for i in range (0,n-1):
    print("i:",i)
    for j in range (i+1,n):
        print("j:",j)
        if lista[i]>lista[j]:
            pom=lista[i]
            lista[i]=lista[j]
            lista[j]=pom
            
print(lista)

"""

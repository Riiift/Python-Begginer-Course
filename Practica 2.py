                                                                   PRACTICA N°2
#---------------------------------------------------------------------------------------------------------------------------------------

EJ1 

import math

def areadeltriangulo(a,b,c):

    p=(a+b+c/2)
    area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area
    
def main():
     
    lado1=float(input("ingrese lado 1:"))
    lado2=float(input("ingrese lado 1:"))
    lado3=float(input("ingrese lado 1:"))
    
    resultado= areadeltriangulo (lado1,lado2,lado3)
    
    print("El area es: {:.2f}".format(resultado)) #*PREGUNTAR*¨LO DE .2F
    
main()
#-----------------------------------------------------------------------------------------------------

EJ2
import math

def raiz(r,i):
    
    calculoraiz = math.pow(r, 1/i)
    
    return calculoraiz
        
def main():
    
    radicando=float(input("Ingrese el redicando (numero real): "))
    indice=int(input("Ingrese el indice (numero natural): "))
    
    resultado= raiz(radicando, indice)
    
    print("La raiz de indice: {} y de radicando: {} es: {:.2f} ".format(indice,radicando,resultado))
           
main()

#-----------------------------------------------------------------------------------------------------
EJ3
numbinario=input("Ingrese un numero de binario de hasta 8 bits: ")
#-----------------------------------------------------------------------------------------------------
EJ6
import random

def azar(v,t):
    
    randomgenrator=random.randint(0,1)
           
    return randomgenrator

def main():
    
    a=input("Ingrese alternativa 1 para vestimenta:")
    b=input("Ingrese alternativa 2 para vestimenta:")
    c=input("Ingrese alternativa 1 para plato:")
    d=input("Ingrese alternativa 2 para plato:")
    e=input("Ingrese alternativa 1 para bebida:")
    f=input("Ingrese alternativa 2 para bebida:")
    
    #ropa
    vestrana=azar(a,b)*b
    vestranb=azar(a,b)*a
    
    #plato
    paltoranc=azar(c,d)*d
    paltorand=azar(c,d)*c
    
    #bebida
    bebidarane=azar(e,d)*d
    bebidarand=azar(e,d)*e
  
    print()
    print('cena al azar:" {0!s}{1!s}, {2!s}{3!s} y {4!s}{5!s}'.format(vestrana,vestranb,paltoranc,paltorand,bebidarane,bebidarand))

       
main()

EJ7

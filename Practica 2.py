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
    
    print("El area es: {:.2f}".format(resultado))
    
main()
#-----------------------------------------------------------------------------------------------------

EJ2




import random

def azar():
    
    random=random.randint(0,1)
    return random

def main():
    
    a=input("Ingrese alternativa 1 para vestimenta:")
    b=input("Ingrese alternativa 2 para vestimenta:")
    c=input("Ingrese alternativa 1 para plato:")
    d=input("Ingrese alternativa 2 para plato:")
    e=input("Ingrese alternativa 1 para bebida:")
    f=input("Ingrese alternativa 2 para bebida:")
    
    rand= azar(a+b)
    
    print()
    print("cena al alazar: {}, {} y {}").format()

       
main()

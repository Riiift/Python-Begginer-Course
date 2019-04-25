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

def pariedad(a,b,c,d,e,f,g,h):
    
    suma=(a+b+c+d+e+f+g+h)
    modulo=suma%2
    
    return modulo

def main():
    
    numbinario = int(input("Ingrese un numero de binario de hasta 8 bits: "))

    h=numbinario%10
    g=(numbinario//10)%10
    f=(numbinario//100)%10
    e=(numbinario//1000)%10
    d=(numbinario//10000)%10
    c=(numbinario//100000)%10
    b=(numbinario//1000000)%10
    a=(numbinario//10000000)%10
    
    pariedadresult=pariedad(a,b,c,d,e,f,g,h)
    
    print("Bit de paridad generado :",pari)
    
main()

#-----------------------------------------------------------------------------------------------------

EJ4

import math

def areaCirc(d):
    
    diametro=d
    radio= diametro/2
    area= math.pi*radio**2
    
    return area

def areaCuad(lado):
    
    ac= lado*lado
    
    return ac

def areaNegra(lado):
    
    areablanca=areaCirc(8) + areaCirc(4) + areaCirc(4)    
    areaNegra= areaCuad(lado) - areablanca
    
    return areaNegra

def main():
    
    lado= float(input("ingrese el lado: "))
              
    an= areaNegra(lado)
    poran= an*100/areaCuad(lado)
              
    print("El area negra es {:.2f} y es un {:.2f}% del area total del cuadrado".format(an,poran))
    
main()


#-----------------------------------------------------------------------------------------------------
EJ5

import random

def lim(input1, input2):

    Rnum = random.randint(input1, input2)
    return Rnum 

def main ():

    liminferior = (int(input("Ingrese el limite inferiror: ")))
    limsuperior = (int(input("Ingrese el limite superior: ")))

    limx = lim(liminferior, limsuperior)
    limy = lim(liminferior, limsuperior)
    limz = lim(limx, limy)

    print()
    print(("1-limite inferior {} limite superior {} numero generado:{}").format(liminferior,limsuperior,limx))
    print(("2-limite inferior {} limite superior {} numero generado:{}").format(liminferior,limsuperior,limy))
    print(("3-limite inferior {} limite superior {} numero generado:{}").format(limx,limy,limz))
 
main ()

#----------------------------------------------------------------------------------------------------------------

EJ6

import random

def azar():
    
    randomgenrator=random.randint(0,1)
           
    return randomgenrator

def main():
    
    a=input("Ingrese alternativa 1 para vestimenta:")
    b=input("Ingrese alternativa 2 para vestimenta:")
    c=input("Ingrese alternativa 1 para plato:")
    d=input("Ingrese alternativa 2 para plato:")
    e=input("Ingrese alternativa 1 para bebida:")
    f=input("Ingrese alternativa 2 para bebida:")
    
    s1 = azar()
    s2 = azar()
    s3 = azar()

    vestimenta = s1*a + b*(1 - s1)
    plato = s2*c + d*(1 - s2)
    bebida = s3*e + f*(1 - s3)
  
    print()
    print('Cena alazar: {0!s:} , {1!s:} y {2!s:}'.format(vestimenta,plato,bebida))
    
main()

#-------------------------------------------------------------------------------------------------------------------------------------

EJ7

def justificado(x,a):
    
    espacio = (x)*a
    
    return espacio

def main():

    frase = input("Ingrese la frase:" )
    ancho = int(input("Ingrese el ancho total a ser usado:" ))
    
    Justif= justificado(' ', ancho-2)

    print ("'{0!s}{1!s}'".format(Justif,frase))

main()

#-------------------------------------------------------------------------------------------------------------------------------------

EJ8 

def crearfila(y):
   
    cantidadancho = ("*")*y + ("\n")
     
    return cantidadancho
    
def crearRectangulo(z,h):
    
    cantidadaltoyancho= crearfila(z)*h
    
    return cantidadaltoyancho
    
def main():
    
    ancho= int(input('Ingrese Ancho: '))
    alto= int(input('Ingrese Alto: '))

    print(crearRectangulo(ancho,alto))
                  
main()

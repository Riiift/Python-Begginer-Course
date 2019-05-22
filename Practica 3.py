                                                                   PRACTICA N°3
#---------------------------------------------------------------------------------------------------------------------------------------

EJ1 

def caculadora(n1,n2,ope):
        
    if ope == "+":
        resultado= n1 + n2
        
    elif ope == "-":
        resultado= n1 - n2
        
    elif ope == "*":
        resultado= n1*n2
        
    elif ope == "/":    
        resultado= n1/n2
    
    return resultado

def main():
    
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el primer numero: "))
    ope = (input("Ingrese la operacion(+,-,*,/): "))
    resultadoopera= caculadora(num1,num2,ope)
    print("{}".format(resultadoopera))

main()

#---------------------------------------------------------------------------------------------------------------------------------------

EJ2

#---------------------------------------------------------------------------------------------------------------------------------------

EJ3

def positivo_negativo(n):
    if(n>0):
        r="Positivo"
    elif n<0:
        r="Negativo"
    else:
        r="Cero es"
    
    return r

def entero(n):
    if(n%1==0):
        if (n>0) and (n<=9):
            r="Entero Natural"
        else:
            r="Entero"
    else:
        r="real"
    return r

def main():
    num=float(input("Ingrese un numero: "))
    pos_neg= positivo_negativo(num)
    num_entero= entero(num)
    print("El numero es {} {}".format(pos_neg,num_entero))
main()


#---------------------------------------------------------------------------------------------------------------------------------------
EJ4

def main ():
    num_a= int(input("ingrese nuemro A: " ))
    num_b= int(input("ingrese nuemro B: " ))
    if verificador(num_a,num_b)== True:
        print ("SI cumple con la funcion")
    else:
        print("NO cumple con la funcion")
main()
#---------------------------------------------------------------------------------------------------------------------------------------

EJ5

def bisiesto(d,m,a):
    
    if (d <=30 and d>=1 ) and (m<=12 and m>=1):
        if a=a%4 and not a
    
        return True
    else
        return False
    


def main():
    dia=int(input("Ingrese dia"))
    mes=int(input("Ingrese mes"))
    año=int(input("Ingrese año"))
    checkeo=bisiesto(dia,mes,año)
    
main()

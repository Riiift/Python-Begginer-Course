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
ef clasi(num):
    
    if num=(0):
        print ("El numero es cero y entero")
        if num >0:
            print ("El numero es positivo y entero")
        if num>0 and num in range (1, 9 ):
            print("El numero es positivo y entero natural")
        if num<0:
            print ("El numero es negativo y entero")
    
def main():
    num=input("Ingrese numero: ")
    clasi(num)
    
    
main()
def verificador(a,b):
    if a<b:
        may=b
        men=a
    elif a>b:
        may=a
        men=b
        
        resta= may-men
            if resta<may and resta>men
                return True
            else:
                return False
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

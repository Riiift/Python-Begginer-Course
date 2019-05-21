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

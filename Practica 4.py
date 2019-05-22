                                                           PRACTICA N°4
#----------------------------------------------------------------------------------------------------------------------------------

EJ1

num = int(input("Ingrese numero entero: "))
cont=0

while cont < 5 :
    num = int(input("Ingrese numero entero: "))
    
    if num%2 == 0:
        cont+=1
        mensaje = ("Numero par. Total de numeros pares ingresados {}".format(cont))
      
        
        if num%4 == 0:
            mensaje = ("Numero par. Tambien es multiplo de '4'. Total de numeros ingresados {}".format(cont))
            
        print (mensaje)
        
print ("\nFIN")
    

#----------------------------------------------------------------------------------------------------------------------------------

EJ2 

def main():

    primero = 0
    print("Ingrese numero enteros positivos (finalice con 0): ", end= '')
    num = int(input())

    while num !=0:
        while num < 0:
            num = int(input("Error, ingrese un numero positivo"))

        if num != 0:            
            if primero == 0:
                menor = num
                mayor = num
                primero+=1                
            if num < menor :
                menor = num                    
            if num > mayor:
                mayor = num               
            num=int(input())
            
    if primero !=0:
        print("El mayor es {} y el menor es {} .".format(mayor, menor))
    else:
        print ("No se ingresaron datos")

main()

#----------------------------------------------------------------------------------------------------------------------------------

EJ3

def primo (n):
    
    cont=0
    
    for i in range (1, n+1):
        if n%i == 0:
            cont+=1
            
    if cont == 2:
        cumple = True
    else:
        cumple = False
          
    return cumple

def main ():
    
    hasta= int(input("Ingrese Numero: "))
    
    for num in range (hasta+1):
        if primo(num) == True:
            print (num,  end='  ')
               
main()
#----------------------------------------------------------------------------------------------------------------------------------

EJ4
def perfecto(n):
    
    i=1
    perfecto=0
    
    while n>i:
        if n%i==0:
            perfecto+=i
        i+=1
        
    if n==perfecto:
        return True

    else:
        return False

def main():
    
    cont=0
    j=1
    
    while cont<10:
        if perfecto(j):
            print(j, end=" ")
            cont+=1
        j+=1
    
main()

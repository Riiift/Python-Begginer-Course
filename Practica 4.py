                                                           PRACTICA N°4
#----------------------------------------------------------------------------------------------------------------------------------

EJ1

num = int(input("Ingrese numero entero: "))
cont=0

while num%2 !=0 :
    num = int(input("Ingrese numero entero: "))
    
if num%2 == 0 :
    cont+=1
    print("Numero par. Total de numeros ingresados {}".format(cont))
    
    if num%4 == 0:
        print("Numero par.Tambien es multiplo de '4'. Total de numeros ingresados {}".format(cont))
 


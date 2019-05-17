                                                         PRACTICA N°5
#------------------------------------------------------------------------------------------------------------------------------

EJ1
 
def divisor(palabra):
    
    if len(palabra) >= 2:
        long= len(palabra)
        pal= palabra
        ult_dig=palabra[(long-2):long]
        x=ult_dig*3
        return x
    
          
    else:
        print ("la funcion ha retornado palabra vacia.")
        
def main():
    palabra = input("Ingrese Palabra: ")
    palabra_div= divisor(palabra)
    print("la funcion ha retornado: {} ".format(palabra_div))
main()

#------------------------------------------------------------------------------------------------------------------------------
EJ2

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

#--------------------------------------------------------------------------------------------------------------------
EJ2

def concatinador(extremos,palabra):
    
    long_extr= len(extremos)
    long_pal= len(palabra)
    e=extremos
    p=palabra
    
    


def main():
    extremos = input("Ingrese extremos: ")
    palabra = input("Ingrese Palabra: ")
    
    print("la funcion ha retornado: {} ".format())
main()
#--------------------------------------------------------------------------------------------------------------------
EJ3

def primerMitad(s):
    div=s[:(len(s)//2)]
    return div

def main():
    pal=input("Ingrese palabra par:")
 while len(pal)%2==1:
    input("ERROR.Ingrese una palabra par, porfavor:")
    while len(pal)%2==0:
        print("La funcion ha retornado:",primerMitad(pal))    
        
main()

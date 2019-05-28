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

#--------------------------------------------------------------------------------------------------------------------
EJ4
def a_minúscula(t):
    cont=""
    for i in range(len(t)):
        if ('A'<=t[i] and t[i]<='Z'):
            cont=cont+chr(ord(t[i])+32) #Convertir mayúsculas a minúsculas
        else:
            cont=cont+t[i] #Si son minúsculas, espacios o signos sigue contando
    return cont
            
def es_letra(pal):
    band=True
    for i in range(len(pal)): 
        if not ('A'<=pal[i] and pal[i]<='Z') or ('a'<=pal[i] and pal[i]<='z'): 
            band=False
    return band

def PrincipioFin(t):
    primera=""
    ultima=""
    i=0
    t=a_minúscula(t)
    while not es_letra(t[i]):
        i = i + 1
    while es_letra(t[i]):
        primera=primera+t[i]
        i=i+1
    i=-1
    while not es_letra(t[i]):
        i=i-1
    while es_letra(t[i]):
        ultima=t[i]+ultima
        i=i-1
    if primera==ultima:
        return True
    else:
        return False

def main():
    texto=input("Ingrese un texto: ")
    if PrincipioFin(texto) == True:
        print("El texto cumple la condición")
    else:
        print("El texto no cumple la condición")


main()


#--------------------------------------------------------------------------------------------------------------------
EJ5
def Rotación(texto):
    l=len(texto)
    nuevo=""
    mitadi=texto[:l // 2] #Texto desde la posición cero hasta la mitad incluída
    mitadf=texto[l // 2:] #Texto desde la mitad excluída hasta el final incluído 
    nuevo=mitadf+mitadi
    return nuevo

def main():
    texto=str(input("Ingrese un texto: "))
    while len(texto)%2!=0 or len(texto)<2:
        texto=str(input("Error. Ingrese un texto: "))
    print("\nLa función ha retornado: ",Rotación(texto))

main()
#--------------------------------------------------------------------------------------------------------------------
EJ6

def esLetra(l):
    if ("A"<=l and l<="Z") or ("a"<=l and l<="z") or l=="Á" or l=="É" or l=="Í" or l=="Ó" or l=="Ú" or l=="á" or l=="é" or l=="í" or l=="ó" or l=="ú":
        return True
    else:
        return False

def palíndroma(t):
    nuevaPalabra=str()
    for i in range(0,len(t)):
        if esLetra(t[i])==True: #Discriminar los espacios y/o signos
            if t[i]=="Á" or t[i]=="á":
                nuevaPalabra=nuevaPalabra+"a"
            elif t[i]=="É" or t[i]=="é":
                nuevaPalabra=nuevaPalabra+"e"
            elif t[i]=="Í" or t[i]=="í":
                nuevaPalabra=nuevaPalabra+"i"
            elif t[i]=="Ó" or t[i]=="ó":
                nuevaPalabra=nuevaPalabra+"o"
            elif t[i]=="Ú" or t[i]=="ú":
                nuevaPalabra=nuevaPalabra+"u" #Reemplazar a las vocales con tilde por vocales sin tilde
            else:
                nuevaPalabra=nuevaPalabra+t[i]
    for x in range(0,len(nuevaPalabra)):
        if nuevaPalabra[x]!=nuevaPalabra[-1-x] and nuevaPalabra[x]!=chr(ord(nuevaPalabra[-1-x])-32) and nuevaPalabra[x]!=chr(ord(nuevaPalabra[-1-x])+32):
            return False
    return True

#chr(número)=Caracter y ord(caracter)=Número
# nuevaPalabra[x]!=chr(ord(nuevaPalabra[-1-x])-32) devuelve si la letra mayúscula es distinta a la letra minúscula
# nuevaPalabra[x]!=chr(ord(nuevaPalabra[-1-x])+32) devuelve si la letra minúscula es distinta a la letra mayúscula

def main():
    t=str(input("Ingrese una frase: "))
    if palíndroma(t)==True:
        print("La frase es palíndroma")
    else:
        print("La frase no es palíndroma")
main()

#--------------------------------------------------------------------------------------------------------------------
EJ7

#Otra forma de resolverlo
"""def contar(tl,tc):
    tl=tl.lower()
    tc=tc.lower()
    l=len(tc)
    cont=0
    pos=tl.find(tc,0,len(tl))
    while pos!=-1:
        if (pos==0 and (not tl[pos + l].isalpha())) or (pos + l == len(tl)  and (not tl[pos -1].isalpha())) or pos + l < len(tl) and pos-1 >= 0 and (not tl[pos + l].isalpha()) and (not tl[pos -1].isalpha()):
            cont = cont + 1
        pos = pos + l
        pos = tl.find(tc, pos, len(tl))
    return cont"""

def a_minuscula(t): #Convertir mayúsculas en minúsculas
    tn=""
    for i in range(len(t)):
        if ('A'<=t[i] and t[i]<='Z'):
            tn=tn+chr(ord(t[i])+32)
        else:
            tn=tn+t[i]
    return tn

def es_letra(pal):
    for i in range(len(pal)):
        if ('A'<=pal[i] and pal[i]<='Z') or ('a'<=pal[i] and pal[i]<='z'):
            return True
    return False

def contar(tl,tc):
    tl=a_minuscula(tl) #Texto corto
    tc=a_minuscula(tc) #Texto largo
    cont=0
    longi=len(tc) #Longitud del texto corto
    longitud=len(tl) #Longitud del texto largo
    i=0
    while i<=(longitud-longi): #La "i" recorre el texto largo y analiza si el texto corto está adentro
        str=tl[i:i+longi] 
        if tc==str:
            cont=cont+1 
        i=i+1
    return cont
   
def main():
    textoLargo=str(input("Ingrese el texto largo: "))
    textoCorto=str(input("Ingrese el texto corto: "))
    print("El texto corto se encontró {:d} veces en el texto largo".format(contar(textoLargo,textoCorto)))

main()

#Otra forma más fácil de resolverlo
"""def buscar(a,b):
    cont=int()
    for i in range (0,len(a)):
        if (a[i:i+len(b)]==b):
            cont=cont+1
    return cont
    
def main():
    a=str(input("Ingrese el texto largo: "))
    b=str(input("Ingrese el texto corto: "))
    print ("El texto corto se encontró",buscar(a,b),"veces en el texto largo")
    
main()"""

#--------------------------------------------------------------------------------------------------------------------
EJ8
#Otra forma de resolverlo con la función str "title"
"""def convertir(texto):
    texto=texto.title()
    return texto
    
def main():
    texto=str(input("Ingrese un texto: "))
    print ("La función ha retornado:",convertir(texto))
main()"""

def a_mayúscula(t): #Convertir minúsculas en mayúsculas
    cont=""
    for i in range(len(t)):
        if ('a'<=t[i] and t[i]<='z'):
            cont=cont+chr(ord(t[i])-32)
        else:
            cont=cont+t[i]
    return cont

def es_letra(pal):
    for i in range(len(pal)):
        if ('A'<=pal[i] and pal[i]<='Z') or ('a'<=pal[i] and pal[i]<='z'):
            return True
    return False

def convertir(t):
    texto=""
    longi=len(t)
    i=0
    while i<longi:
        while i<longi and es_letra(t[i])==False:
            texto=texto+t[i]
            i=i+1
        aux=0
        while i<longi and es_letra(t[i])==True:
            if aux==0:
                texto=texto+a_mayúscula(t[i])
            else:
                texto=texto+t[i]
            i=i+1
            aux=1
    return texto

def main():
    texto = input("Ingrese un texto: ")
    print("la función ha retornado: {}".format(convertir(texto)))

main()

#--------------------------------------------------------------------------------------------------------------------
EJ9

def es_letra(pal):
    for i in range(len(pal)):
        if ('A'<=pal[i] and pal[i]<='Z') or ('a'<=pal[i] and pal[i]<='z') or pal=="Á" or pal=="É" or pal=="Í" or pal=="Ó" or pal=="Ú" or pal=="á" or pal=="é" or pal=="í" or pal=="ó" or pal=="ú":
            return True
    return False

def contar(t): #Cuenta la cantidad de palabras
    l=len(t)
    i=0
    cont=0
    while i<l:
        while i<l and es_letra(t[i])==False:
            i=i+1
        band=0
        while i<l and es_letra(t[i])==True:
            band=1
            i=i+1
        if band==1:
            cont=cont+1
    return cont

def mayor(t): #Palabra de mayor longitud
    l=len(t)
    i=0
    may=0
    palmay=""
    while i<l:
        while i<l and es_letra(t[i])==False:
            i=i+1
        cont=0
        pal=""
        while i<l and es_letra(t[i])==True:
            pal=pal+t[i]
            i=i+1
            cont=cont+1
        if cont>may:
            may=cont
            palmay=pal
    return palmay

#--------------------------------------------------------------------------------------------------------------------
EJ10
def es_letra(pal):
    for i in range(len(pal)):
        if ('A'<=pal[i] and pal[i]<='Z') or ('a'<=pal[i] and pal[i]<='z') or pal=="Á" or pal=="É" or pal=="Í" or pal=="Ó" or pal=="Ú" or pal=="á" or pal=="é" or pal=="í" or pal=="ó" or pal=="ú":
            return True
    return False

def comparar(pal, p): #La palabra está contenida en el texto y y el texto está contenido en la palabra
    for i in range(len(pal)):
        if pal[i] not in p:
            return False
    for i in range(len(p)):
        if p[i] not in pal:
            return False
    return True

def buscar(t, pal):
    l=len(t)
    i=0
    while i<l:
        while i<l and es_letra(t[i])==False:
            i=i+1
        p=""
        while i<l and es_letra(t[i])==True:
            p=p+t[i]
            i=i+1
        if comparar(pal, p)==True:
            return True
    return False

def main():
    texto=input("Ingrese el texto: ")
    palabra=input("Ingrese la palabra: ")
    if buscar(texto, palabra)==True:
        print("\nSe cumple con la condición")
    else:
        print("\nNo se cumple con la condición")

main()

-------------------------------------------------------------------END--------------------------------------------------------------






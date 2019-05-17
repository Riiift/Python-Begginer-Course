def a_mayuscula(letra):
    
    if(letras >= "a" and letras <="z"):
        letra= chr(ord(letra) - (ord("a") - ord("A")))
        
    return letra

def es_letra(c):
    
    if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
        return True
    
    else:
        False
        
def texto_cap(texto):
    texto_pri_mayus=""
    i=0
    while i <len(texto):
       while(i<len(texto)) and not (es_letra(texto[i])):
           texto_pri_masyu +=texto [i]
           i+=1
        primera=1
        while(i<len(texto) and es_letra(texto[i]))):
        
            if primera == 1
                texto_pri_mayus +=a_mayuscula(texto[i])
                primera = 0
            else:
                texto_pri_mayus += texto[i]
            i+=1
return texto_pri_mayus


def main():
    texto= (" Presiona la tecla alt en tu teclado, y no la sueltes. 2) Sin dejar de presionar Alt, presiona en el teclado numérico el número ")
main()



       
        
import random

def azar():
    
    random=random.randint(0,1)
    return random

def main():
    
    a=input("Ingrese alternativa 1 para vestimenta:")
    b=input("Ingrese alternativa 2 para vestimenta:")
    c=input("Ingrese alternativa 1 para plato:")
    d=input("Ingrese alternativa 2 para plato:")
    e=input("Ingrese alternativa 1 para bebida:")
    f=input("Ingrese alternativa 2 para bebida:")
    
    rand= azar(a+b)
    
    print()
    print("cena al alazar: {}, {} y {}").format()

       
main()
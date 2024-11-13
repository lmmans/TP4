import random

p = [6,2,2,3] ##polynomial defined as a list
# list [a0, ax, ax^2, ax^3, ax^n]
#x = 3 #value to calculate the polynomial
#in case we just want a random number to appear we can use this:
x = random.randint(1,10) 

def afficher(p):
    n = len(p) - 1 #list lenght -1 to get the maximum degree of the polynomial
    
    for a in range(n, -1, -1): #from higher to lower degree
        c = p[a] #to get the current coefficient
        
        if c != 0:
            if a == 0:#constant, last term without x
                print(c, end="")
            elif a == 1: #term with x without power 
                print(f"{c}x", end="")
            else: #to any term a > 1 so it writes 'x^a'
                print(f"{c}x^{a}", end="")
           
            if a>0:
                print(" + ", end="")
                

## 1.2 fonction qui calcule et renvoie la valeur du polynôme p au point x
def get_valeur(p, x):
    result = 0
    
    for a in range(len(p)-1, -1, -1): #from higher to lower degree
        result = result * x + p[a] 
    return result

## 1.3 fonction qui calcule et retourne le polynôme dérivé du polynôme p
def deriver(p):
    n = len(p)
    derivate = []
    
    for a in range(1, n): #we start from 1 because [a0] is the constant and it's equal to 0
        derivate.append(p[a]*a) #derivate i * coefficient of x^i
    
    afficher(derivate) #call the function
    
    # for a in range(len(derivate)-1, -1, -1): #from higher to lower degree
    #     if a > 0:
    #         print(f"{derivate[a]}x^{a} + ", end="")
    #     else:
    #         print(f"{derivate[a]}")
    
## 1.4 écrire un programme principal pour vérifier le bon fonctionnement de ces 3 fonctions
#funcion que lea p, asigne un valor a x y muestre la derivada de p
print("Test of the functions with the given polynomial and with x =", x)
print("\n"*1)

print("The polynomial is:")            
afficher(p)
print("\n"*1)

valeur = get_valeur(p, x)
print("The value of the polynomial in x =", x, "is: ", valeur)
print("\n"*1)

print("The derivate of the polynomial is: ")
deriver(p)
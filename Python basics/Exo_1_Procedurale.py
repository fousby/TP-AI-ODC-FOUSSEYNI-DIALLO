#Importation de la librarie math
import math

#Definition de la fonction F(x)
def calcul_f(x):
    return (x/(x**2+1))

#Definition de la fonction G(x)
def calcul_g(x):
    return math.atan(x)

#Le nombre à traiter
N= int(input("Entrez un nombre : "))

#La liste à generer
l1 =list(range(-N, N+1))
print(l1)


# Definition de la fonction qui calcul de R
def somme_function():
    R=0
    for i in l1:
        R+=(calcul_f(i)-calcul_g(i))**2
    return R
print(somme_function())
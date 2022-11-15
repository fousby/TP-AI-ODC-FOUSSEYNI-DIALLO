#Importation du module Random
import random

#Definition de la fonction f(x)
def function_f(x):
    return (x**3+3*(x**2)-5)

#Definition de la grande liste, la taille des sous-liste ainsi que le nombre de sous liste
D=[]
S=int(input("Entrez une Taille : "))
n=int(input("Entrez le nombre de sous liste : "))


#Definition de la fonction qui cree les sous listes
def create_liste():
    for i in range(n):
        l=[]
        for j in range(S):
            number = random.randint(0,50)
            l.append(number)
        D.append(l)
    print(D)
create_liste()


#Definition de la fonction qui calcule la valeur minimal pour chaque sous liste
def min_list(L,t):
    minV=L[0]
    for i in range(t):
        if(minV>L[i]):
            minV=L[i]
    return minV

#Definition de la fonction qui calcule la valeur maximal pour chaque sous liste
def max_list(L,t):
    maxV=L[0]
    for i in range(t):
        if(maxV<L[i]):
            maxV=L[i]
    return maxV
#Declaration des variables qui vont contenir les valeur minimal et maximal de la liste globale
minGlobalD=[]
maxGlobalD=[]

#Calcul de la valeur minimal de la liste dans sa globalité
print("Les minimum des listes de D sont: ")
for i in range(n):
    minG = min_list(D[i],S)
    print(minG)
    minGlobalD.append(minG)

#Calcul de la valeur maximal de la liste dans sa globalité
print("Les Maximum des listes de D sont: ")
for i in range(n):
    maxG= max_list(D[i],S)
    print(maxG)
    maxGlobalD.append(maxG)

#Le resultat de la valeur minimal de la liste dans sa globalite
print("Le minimum Global de D est: ")
print(min_list(minGlobalD,n))

#Le resultat de la valeur maximal de la liste dans sa globalite
print("Le Maximum Global de D est: ")
print(max_list(maxGlobalD,n))

#Definition de la fonction qui permet de cacul D'
def lacalcul_D():
    Dprime= []
    for i in range(n):
        l=[]
        for j in range(S):
            l.append(function_f(D[i][j]))
        Dprime.append(l)
    print(Dprime)

#Le resultat de la valeur de D'
print("Les valeurs de D' :")
lacalcul_D()
    

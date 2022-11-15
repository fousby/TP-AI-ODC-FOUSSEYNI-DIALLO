#Importation de la librarie random
import random
#Importation de la librarie statistics
import statistics
#Declaration de la liste et de la taille
L = []
S = 100

#Definition de la fonction qui genere la liste avec les contenus aléatoire
def generator():
    for t in range(S):
        number = random.random()
        L.append(number)
    print("la liste est :")
    print(L)
generator()

#Definition de la fonction qui calcule la moyenne
def moy():
    moyenne=(statistics.mean(L))
    print("la moyenne de cette liste est :")
    print(moyenne)
moy()

#Definition de la fonction qui calcule la medianne
def medianne():
    medianne=(statistics.median(L))
    print("la medianne de cette liste est :")
    print(medianne)
medianne()

#Definition de la fonction qui calcule la variance
def variance():
    variance=(statistics.variance(L))
    print('la variance de cette liste est :')
    print(variance)
variance()

#Definition de la fonction qui calcule l'ecart type
def ecart_type():
    ecart_type=(statistics.pstdev(L))
    print("l'ecart_type de cette liste est :")
    print(ecart_type)
ecart_type()
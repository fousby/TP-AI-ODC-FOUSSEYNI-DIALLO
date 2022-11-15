#Importation de la librarie math
import math

class Exo1:
    # Definition du constructeur
    def __init__(self):
        self.l1 = None
        self.N = 0

    # Definition de la fonction F(x)
    def calcul_f(self,x):
        return (x / (x ** 2 + 1))

    # Definition de la fonction G(x)
    def calcul_g(self,x):
        return math.atan(x)

    #Definition de la fonction qui genere la liste
    def create_liste(self):
        self.l1=[]
        try :
            self.N = int(input("Entrez un nombre : "))

        except ValueError:
            print('Valeur incompatible')

        for i in range(-self.N, self.N + 1):
            self.l1.append(i)
        print("La liste : ")
        print(self.l1)



    #Definition de la fonction qui calcul de R
    def somme_function(self):
        R = 0
        for i in self.l1:
            R += (self.calcul_f(i) - self.calcul_g(i)) ** 2
        return R



d1= Exo1()

d1.create_liste()

print(d1.somme_function())


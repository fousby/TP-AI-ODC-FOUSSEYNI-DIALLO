#Importation du module Random
import random

#Definition de la class DataTrans
class DataTrans:


    # Definition de la fonction f(x)
    def function_f(self,x):
        return (x ** 3 + 3 * (x ** 2) - 5)
    #Declaration du constructeur
    def __init__(self):
        self.D = None

    def __int__(self):
        self.D= None
        self.n=0
        self.S=0

    #Definition de la fonction qui cree les sous listes
    def create_liste(self):
        try:
            S = int(input("Entrez une Taille : "))
            n = int(input("Entrez le nombre de sous liste : "))
        except :
            S=0
            n=0
            print('Valeur incompatible')


        self.D=[]
        self.S = S
        self.n = n

        for i in range(self.n):
            l = []
            for j in range(self.S):
                number = random.randint(0, 50)
                l.append(number)
            self.D.append(l)
        print(self.D)


    # Definition de la fonction qui calcule la valeur minimal pour chaque sous liste
    def min_list(self,L,t):
        minV = L[0]
        for i in range(t):
            if (minV > L[i]):
                minV = L[i]
        return minV


    # Definition de la fonction qui calcule la valeur maximal pour chaque sous liste
    def max_list(self, L,t):
        maxV = L[0]
        for i in range(t):
            if (maxV < L[i]):
                maxV = L[i]
        return maxV

    # Definition de la fonction qui calcule les valeurs minimals et maximals de la liste dans sa globalité
    def max_and_min(self):
        try:
            minGlobalD = []
            maxGlobalD = []
            for i in range(self.n):
                minG = self.min_list(self.D[i],self.S)
                minGlobalD.append(minG)

            for i in range(self.n):
                maxG = self.max_list(self.D[i],self.S)
                maxGlobalD.append(maxG)
            # Le resultat de la valeur minimal de la liste dans sa globalite
            print("Le minimum Global de D est: ")
            print(self.min_list(minGlobalD,self.n))
            # Le resultat de la valeur maximal de la liste dans sa globalite
            print("Le Maximum Global de D est: ")
            print(self.max_list(maxGlobalD,self.n))
        except IndexError:
            print("Probleme d'indice")
    # Definition de la fonction qui permet de cacul D'
    def lacalcul_D(self):
        try :
            Dprime = []
            for i in range(self.n):
                l=[]
                for j in range(self.S):
                    l.append(self.function_f(self.D[i][j]))
                Dprime.append(l)
            print(Dprime)
        except IndexError:
            print("Probleme d'indice survenu")



d1 = DataTrans()
d1.create_liste()
print("Le minimum de chaque liste  :")
for i in range(d1.n):
    print(d1.min_list(d1.D[i],d1.S))
print("Le maximum de chaque liste  :")
for i in range(d1.n):
    print(d1.max_list(d1.D[i],d1.S))
d1.max_and_min()
print("Les valeurs de D' :")
d1.lacalcul_D()

reponse = 'oui'
#la boucle qui permettra de continuer le programme
while(reponse == 'oui'):

    #identification de l'utilisateur
    nom=input("Entrez un nom : ")
    utilisateur=print("Salut ",nom)

    #le choix du programme qu'il veut executer

    n=int(input("Entrez l'exercice que vous voulez faire, (1 OU 2)  :"))


    #la condition qui determinera le choix
    if n == 1:
        #importation du script 1
        import Exo1OO
    elif n == 2:
        # importation du script 2
        import classDataTrans
    else:
        print("Votre demande est non prise en compte par le systeme")
    reponse = input("Voulez-vous continuez ?: (o/n)")




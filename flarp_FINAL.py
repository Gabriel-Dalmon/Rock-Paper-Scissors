#DÉBUT
#           
#admettre que l'exécution de la fonction [choice] retourne un élément aléatoire d'une liste donnée en paramètre
#admettre que l'exécution de la fonction [input] retourne une donnée de type (string) au joueur existe
#               
#définir [convertirChoix] avec pour paramètre (choix, choixPossibles) #commentaire : convertit l'input du joueur en un index pour le manipuler plus facilement
#   pour tous les (index) entre 0 et la longueur de la liste (choixPossibles)
#       si (choix) est égal à l'élément de (choixPossibles) d'index (index)
#           alors retourner (index)
#               
#               
#               
#définir la fonction [calculerVainqueur] recevant en paramètre choixJ1, choixJ2 et choixPossibles 
#    si choixJ1 est égal à (choixJ2)
#        alors retourner NULL
# 
#    #commentaire : grâce à l'exécution de [convertirChoix], on teste si l'index du choix du joueur 1 est supérieur d'une différence d'1 à l'index du choix du joueur 2 ou si l'index du choix du joueur 1 correspond au premier item de la liste choixPossibles et de joueur 2 au dernier item.
#    #commentaire : ce choix simplifie les testes d'assertions en cas de victoire et offre une flexibilité pour éventuellement composer une liste (choixPossibles) plus longue ; exemple : ["LOUP", "RENARD", "POULE", "VIPÈRE"] 
#    sinon si ((choixJ1) moins (choixJ2) est égal à 1) ou (((choixJ1) moins (choixJ2)) est égal (à moins le retour de l'exécution de la fonction longueur avec (choixPossibles) en paramètre additionné à 1))
#        alors retourner 0
#    sinon
#        alors retourner 1
#           
#           
#définir la fonction [pfc] recevant en paramètres (nbVictoire) décrivant le score à atteindre pour un joueur pour gagner la partie, (nomJoueur1), (nomJoueur2)
#                   
#    initialiser la liste (choixPossibles) définissant les trois valeurs attendues du retour d'un joueur, soit une liste composée de "PIERRE", "FEUILLE" et "CISEAUX"
#               
#    initialiser le tableau (Joueurs) qui est composé de deux dictionnaires ayant pour clés (nom), (score) et (dernierChoix). 
#    assigner (nomJoueur1) comme valeur à la clé (nom) du premier élément de (Joueurs)
#    assigner (nomJoueur1) comme valeur à la clé (nom) du second élément de (Joueurs)
#    assigner 0 aux les clés (score) de chaque élément de (Joueurs) et assigner NULL aux les clés (dernierChoix) de chaque élément de (Joueurs).
#                           
#    tant que nbVictoire est différent de la valeur de la clé (score) pour les deux éléments du tableau
#        initialiser puis réinitialiser à chaque itération la variable (joueurInput)
#        alors pour tous les éléments dans le tableau (Joueurs)
#            tant que la valeur de (joueurInput) n'est pas égal à l'un des éléments de (choixPossible)
#                alors si la valeur à la clé (nom) du joueur actif est égal à "CPU"
#                    alors assigner à la valeur de (joueurInput) la valeur retournée par l'exécution de la fonction [choice] en donnant en paramètre (choixPossible)
#                sinon 
#                    alors assigner à la valeur de (joueurInput) la valeur retournée par l'exécution de la fonction [input]
#            assigner à la valeur de la clé (dernierChoix) de l'élément actif le retour de l'exécution de la fonction [convertirChoix] avec comme paramètre (joueurInput) et la liste (choixPossibles)
#            
#        #commentaire : lorsque les deux joueurs fait leur choix et que ces choix ont été converti en index de la liste des choix possible 
#        assigner à (indexVainqueur) le retour de l'exécution de la fonction [calculerVainqueur] qui prend en paramètres la valeur de la clé (dernierChoix) dans l'élément d'index 0 de (Joueurs) et en second paramètre dans l'élément d'index 1 de (Joueurs)
#        incrémenter la valeur à la clé (score) de l'élément d'index (indexVainqueur) du tableau (Joueurs)
#       
#        si indexVainqueur est égal à NULL 
#            alors écrire message "Tour nul !"
#        sinon
#            alors écrire message "(valeur à la clé (nom) de l'élément d'index (indexVainqueur) du tableau (Joueurs)) gagne le round !"
#                           
#    #commentaire : lorsque l'un des deux joueurs obtient un score égal au score requis pour une victoire
#    écrire message "(valeur à la clé (nom) de l'élément d'index (indexVainqueur) du tableau (Joueurs)) gagne la partie !"
#
#exécuter la fonction [pfc]
#
#FIN
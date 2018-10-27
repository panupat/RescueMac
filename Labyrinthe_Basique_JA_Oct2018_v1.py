#Soit le labyrinthe composé 10 lignes et 15 sprites (15 cases, cellules ou col). Il est mis dans une liste (laby =[] est une liste de lignes qui se suivent, la ligne = une chaîne de caractères). 
#On voit déjà le chemin que doit prendre le "8" (ie. le "MacGyver" pour en sortir). Ce Laby forme un tableau (comme sur Excel, une position = une cellule) de 15 col. et 10 lignes.
laby = ["*8*************",
        "* *************",
        "*        ******",
        "**** * * ******",
        "*    * * ******",
        "****** * ******",
        "*      * ******",
        "* *************",
        "*        ******",
        "******** ******"]
#Boucle : soit i = une ligne parmi les lignes donnée du laby (les lignes sont précisé dans la liste Laby ci-dessus). 
#Print (laby[i]) = la boucle va imprimer chaque ligne sur laquelle elle passera
for i in range(10) :
    print(laby[i])
 
perso = [0,1]      #position du personnage, sur la ligne (comme sur VBA) : position 0 de ligne, position 1 (+1) de colonne
perso_l = 0        #La variable perso_l = ligne du personnage à 0 i.e. 1ère ligne
perso_c = 1        #La variable perso_c = colonne du personnage à 1 i.e. deuxième colonne (+1) cf. le tableau du labyrinthe ci-dessus.

#Fonction Afficher (est utilisée en fin fin de boucle). Elle affiche le labyrinthe ainsi que la totalité des paramètres intégrés dans la boucle.
#Pour chaque ligne incluse dans le [:total compté des (lignes de Laby)] : le script imprime la ligne
def afficher(laby):
    """affiche un labyrinthe défini comme une liste de chaines"""
    for ligne in laby[:len(laby)]:
        print(ligne)

#Fonction Remplacer
 
def remplacer(chaine,i,car):
    """remplace le ième caractère de la chaine par caractère"""
    s=chaine[:i]+car+chaine[i+1:] #ME SEMBLE COMPLEXE
    return s
 
while (perso_l!=9) or (perso_c!=8) : #Tant que la ligne de position du perso est différente de 9 ou que la colonne de position est différente de 8
    a = input("ou voulez vous aller:(gauche = q, droite = d, haut = z, bas = s)")
    if a == "q": #si le joueur saisi q gauche
        if laby[perso_l][perso_c-1] == "*" : #si Pour la ligne donnée,[perso_l], le caractère de gauche (-1 comme dans VBA, aller sur col. left) = "*"" i.e. le "mur" alors passage bloqué.
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c-1] == " " : #si pour la ligne donnée, le caractère de gauche (-1 comme dans VBA sur la colonne) = " " alors OK on passe à la suite :
            laby[perso_l]=remplacer(laby[perso_l],perso_c-1,"8") #sur la ligne du personnage (ou la chaîne), la position -1 (à gauche) prend donc la valeur 8 (le 8 se déplace bien)
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ") #sur la ligne du personnage (ou la chaîne), la position actuelle (initiale) prend donc la valeur " " (le 8 s'est déplacé)
            perso_c=perso_c-1 #La position du personnage devient la position actuelle - 1 (c'est à dire 1 sprite vers la gauche)
    if a == "d": #si le joueur saisi d droite
        if laby[perso_l][perso_c+1] == "*" : #si Pour la ligne donnée,[perso_l], le caractère de droite (+1 comme dans VBA, aller sur col. rigt) = "*"" i.e. le "mur" alors passage bloqué.
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c+1] == " " : #si pour la ligne donnée, le caractère de droite (+1 comme dans VBA sur la colonne) = " " alors OK on passe à la suite :
            laby[perso_l]=remplacer(laby[perso_l],perso_c+1,"8") #sur la ligne du personnage (ou la chaîne), la position +1 (à droite) prend donc la valeur 8 (le 8 se déplace bien)
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ") #sur la ligne du personnage (ou la chaîne), la position actuelle (initiale) prend donc la valeur " " (le 8 s'est déplacé)
            perso_c=perso_c+1 #La position du personnage devient la position actuelle + 1 (c'est à dire 1 sprite vers la droite)
    if a == "z":
        if laby[perso_l-1][perso_c] == "*" :#si Pour la ligne précédente,[perso_l-1], le caractère du haut (-1 comme dans VBA, aller sur ligne. up) = "*"" i.e. le "mur" alors passage bloqué.
            print("vous ne pouvez pas passer!")
        elif laby[perso_l-1][perso_c] == " " : #si sur la ligne donnée, le caractère du haut (-1 comme dans VBA sur la ligne) = " " alors OK on passe à la suite :
            laby[perso_l-1]=remplacer(laby[perso_l-1],perso_c,"8") #le 8 s'affiche sur sa nouvelle position (ligne - 1 = précédente) suite à l'action de la direction saisie par le joueur
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ") #L'ancienne position du 8 passe à " " soit du vide (normal)
            perso_l=perso_l-1 #La position du personnage devient la position actuelle - 1 (c'est à dire 1 ligne plus haut)
    if a == "s":
        if laby[perso_l+1][perso_c] == "*" : #si Pour la ligne suivante,[perso_l+1], le caractère du haut (-1 comme dans VBA, aller sur ligne. up) = "*"" i.e. le "mur" alors passage bloqué.
            print("vous ne pouvez pas passer!")
        elif laby[perso_l+1][perso_c] == " " : #si sur la ligne donnée, le caractère du bas (+1 comme dans VBA sur la ligne) = " " alors OK on passe à la suite :
            laby[perso_l+1]=remplacer(laby[perso_l+1],perso_c,"8") #le 8 s'affiche sur sa nouvelle position (ligne + 1 = suivante) suite à l'action de la direction saisie par le joueur
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ") #L'ancienne position du 8 passe à " " soit du vide (normal)
            perso_l=perso_l+1 #La position du personnage devient la position actuelle + 1 (c'est à dire 1 ligne plus bas)
    if laby[perso_l] == 9 and laby[perso_c] == 8 : #La position du personnage est ligne 9 (dernière ligne) et colonne 8 (8ième position sur la ligne)
        print("Bravo vous avez terminé") #Ne s'AFFICHE PAS (pb de positionnement, ce test dans le code)
    afficher(laby)
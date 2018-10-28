class Position:
  def __init__(self, line, column):
    self.line = line
    self.column = column


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

def afficher(laby):
    for ligne in laby[:len(laby)]:
        print(ligne)

afficher(laby)
 


perso_l = 0
perso_c = 1
perso = [perso_l, perso_c]      #position du personnage, sur la ligne (comme sur VBA) : position 0 de ligne, position 1 (+1) de colonne



 
def remplacer(chaine,i,car):
    s=chaine[:i]+car+chaine[i+1:] #ME SEMBLE COMPLEXE
    return s

 
while (perso_l!=9) or (perso_c!=8) :
    a = raw_input("ou voulez vous aller:(gauche = q, droite = d, haut = z, bas = s)")
    if a == "q":
        if laby[perso_l][perso_c-1] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c-1] == " " :
            laby[perso_l]=remplacer(laby[perso_l],perso_c-1,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_c=perso_c-1
    if a == "d":
        if laby[perso_l][perso_c+1] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c+1] == " " :
            laby[perso_l]=remplacer(laby[perso_l],perso_c+1,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_c=perso_c+1
    if a == "z":
        if laby[perso_l-1][perso_c] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l-1][perso_c] == " " :
            laby[perso_l-1]=remplacer(laby[perso_l-1],perso_c,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_l=perso_l-1
    if a == "s":
        if laby[perso_l+1][perso_c] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l+1][perso_c] == " " :
            laby[perso_l+1]=remplacer(laby[perso_l+1],perso_c,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_l=perso_l+1
    afficher(laby)
print("Bravo vous avez termine")
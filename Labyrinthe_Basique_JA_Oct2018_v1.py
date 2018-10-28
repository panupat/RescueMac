from random import randint

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



availableCases =    [Position(1, 1), 
                    Position(2, 1), Position(2, 2), Position(2, 3), Position(2, 4), Position(2, 5), Position(2, 6), Position(2, 7), Position(2, 8),
                    Position(3, 4), Position(3, 6), Position(3, 8),
                    Position(4, 1), Position(4, 2), Position(4, 3), Position(4, 4), Position(4, 6), Position(4, 7),
                    Position(5, 6), Position(5, 8),
                    Position(6, 1), Position(6, 2), Position(6, 3), Position(6, 4), Position(6, 5), Position(6, 6), Position(6, 8), 
                    Position(7, 1), 
                    Position(8, 1), Position(8, 2), Position(8, 3), Position(8, 4), Position(8, 5), Position(8, 6), Position(8, 7), Position(8, 8),
                    Position(9, 8)]
 


perso_l = 0
perso_c = 1
perso = [perso_l, perso_c]      #position du personnage, sur la ligne (comme sur VBA) : position 0 de ligne, position 1 (+1) de colonne

def remplacer(chaine,i,car):
    s=chaine[:i]+car+chaine[i+1:] #ME SEMBLE COMPLEXE
    return s

def generateInGameObjets():
    for x in xrange(1, 4):
        index = (randint(0, len(availableCases)))
        position = availableCases[index]
        if x == 1:
            laby[position.line] = remplacer(laby[position.line], position.column, "A") #A=AIGUILLE
        elif x == 2:
            laby[position.line] = remplacer(laby[position.line], position.column, "E") #E=ETHER
        else:
            laby[position.line] = remplacer(laby[position.line], position.column, "T") #T=TUBE EN PLASTIQUE
        availableCases.pop(index)

def afficher(laby):
    for ligne in laby[:len(laby)]:
        print(ligne)

generateInGameObjets()
afficher(laby)

 


 
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
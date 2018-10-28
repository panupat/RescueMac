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
        "********G******"]

def buildAvailPositionList():
	positionList = []
	l = 0
	for line in laby:
		for x in range(0, len(line)):
			print "in 2nd for"
			if line[x] == " ":
				positionList.append(Position(l, x))
		l = l + 1
	return positionList

availableCases = buildAvailPositionList()


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

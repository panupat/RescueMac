from random import randint

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

class Position:
	def __init__(self, line, column):
		self.line = line
		self.column = column

	def __str__(self):
		strToReturn = "line: " + str(self.line) + "\n"
		strToReturn = strToReturn + "column: " + str(self.column) + "\n"
		return strToReturn

	def __eq__(self, other):
		return (self.line == other.line) and (self.column == other.column)


class Perso:
	def __init__(self, pos):
		self.pos = pos


	def __str__(self):
		return "Perso position:\n" + str(self.pos) + "\n"


	def goLeft(self):
		if laby[self.pos.line][self.pos.column - 1] != "*" and self.pos.column > 0:
			newPos = Position(self.pos.line, self.pos.column - 1)
			updatePersoPositionInLaby(self.pos, newPos)
			self.pos = newPos
		else:
			print("You can not go there !")
    	

	def goRight(self):
		if laby[self.pos.line][self.pos.column + 1] != "*" and self.pos.column < len(laby[self.pos.line]) - 1:
			newPos = Position(self.pos.line, self.pos.column + 1)
			updatePersoPositionInLaby(self.pos, newPos)
			self.pos = newPos
		else:
			print("You can not go there !")
    	

	def goUp(self):
		if laby[self.pos.line - 1][self.pos.column] != "*" and self.pos.line > 0:
			newPos = Position(self.pos.line - 1, self.pos.column)
			updatePersoPositionInLaby(self.pos, newPos)
			self.pos = newPos
		else:
			print("You can not go there !")
    	

	def goDown(self):
		if laby[self.pos.line + 1][self.pos.column] != "*" and self.pos.column < len(laby) - 1:
			newPos = Position(self.pos.line + 1, self.pos.column)
			updatePersoPositionInLaby(self.pos, newPos)
			self.pos = newPos
		else:
			print("You can not go there !")


def remplacer(chaine,i,car):
    s=chaine[:i]+car+chaine[i+1:] #ME SEMBLE COMPLEXE
    return s


def updatePersoPositionInLaby(oldPos, newPosition):
	laby[oldPos.line] = remplacer(laby[oldPos.line], oldPos.column, " ")
	laby[newPosition.line] = remplacer(laby[newPosition.line], newPosition.column, "8")


def buildAvailPositionList():
	positionList = []
	l = 0
	for line in laby:
		for x in range(0, len(line)):
			if line[x] == " ":
				positionList.append(Position(l, x))
		l = l + 1
	return positionList

availableCases = buildAvailPositionList()

persoInitPosition = Position(0, 1)
exitPosition = Position(9, 8)
perso = Perso(persoInitPosition)



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
	for ligne in laby:
		print(ligne)

generateInGameObjets()




while (not(perso.pos == exitPosition)):
	afficher(laby)
	a = raw_input("ou voulez vous aller:(gauche = q, droite = d, haut = z, bas = s)")
	if a == "q": #left
		perso.goLeft()
	elif a == "d": #right
		perso.goRight()
	elif a == "z": #up
		perso.goUp()
	elif a == "s": #down
		perso.goDown()
print("Bravo vous avez termine")

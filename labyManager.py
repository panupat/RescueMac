from random import randint
import position as Position

laby = []
availableCases = []
persoInitPosition = None
exitPosition = None


def displayLaby():
	for line in laby:
		print(line)


def replace(inputStrinng, i, char):
    outputString = inputStrinng[:i] + char + inputStrinng[i + 1:]
    return outputString


def removeEndOfLineChar():
	for line in laby:
		indexOfLastChar = len(line) - 1
		if line[indexOfLastChar] == '\n':
			indexOfCurrentLine = laby.index(line)
			line = replace(line, indexOfLastChar, '')
			laby[indexOfCurrentLine] = line


def loadLaby():
	global laby
	with open('./laby02.txt') as file:
		laby = file.readlines()
	file.close()
	removeEndOfLineChar()
	return laby


def findExitPosition():
	for line in laby:
		for x in line:
			if x == 'X':
				return Position.Position(laby.index(line), line.index(x))


def initGame():
	global laby
	laby = loadLaby()	
	global availableCases
	availableCases = buildAvailPositionList()
	generateInGameObjets()
	global persoInitPosition
	persoInitPosition = Position.Position(0, 1)
	global exitPosition
	exitPosition = findExitPosition()



def updatePersoPositionInLaby(oldPos, newPosition):
	laby[oldPos.line] = replace(laby[oldPos.line], oldPos.column, " ")
	laby[newPosition.line] = replace(laby[newPosition.line], newPosition.column, "8")


def generateInGameObjets():
	for x in xrange(1, 4):
		availableCasesCount = len(availableCases)
		index = (randint(0, availableCasesCount))
		if index < availableCasesCount:
			position = availableCases[index]
			if x == 1:
				laby[position.line] = replace(laby[position.line], position.column, "A") #A=AIGUILLE
			elif x == 2:
				laby[position.line] = replace(laby[position.line], position.column, "E") #E=ETHER
			else:
				laby[position.line] = replace(laby[position.line], position.column, "T") #T=TUBE EN PLASTIQUE
			availableCases.pop(index)


def buildAvailPositionList():
	positionList = []
	for line in laby:
		for x in range(0, len(line)):
			if line[x] == " ":
				indexOfCurrentLine = laby.index(line)
				positionList.append(Position.Position(indexOfCurrentLine, x))
	return positionList

def charAtPosition(pos):
	return laby[pos.line][pos.column]


def showWarning():
		print("You can not go there !")
		print("Press enter to continue.")
		_ = raw_input()


from random import randint
import position as Position

class LabyManager:

	LABY = []
	AVAILABLE_CASES = []
	PERSO_INIT_POSITION = None
	EXIT_POSITION = None


	@staticmethod
	def replace(inputStrinng, i, char):
	    outputString = inputStrinng[:i] + char + inputStrinng[i + 1:]
	    return outputString


	@staticmethod
	def showWarning():
			print("You can not go there !")
			print("Press enter to continue.")
			_ = raw_input()


	@classmethod
	def displayLaby(cls):
		for line in cls.LABY:
			print(line)


	@classmethod
	def removeEndOfLineChar(cls):
		for line in cls.LABY:
			indexOfLastChar = len(line) - 1
			if line[indexOfLastChar] == '\n':
				indexOfCurrentLine = cls.LABY.index(line)
				line = LabyManager.replace(line, indexOfLastChar, '')
				cls.LABY[indexOfCurrentLine] = line


	@classmethod
	def loadLABY(cls):
		with open('./LABY02.txt') as file:
			cls.LABY = file.readlines()
		file.close()
		cls.removeEndOfLineChar()


	@classmethod
	def findExitPosition(cls):
		for line in cls.LABY:
			for x in line:
				if x == 'X':
					cls.EXIT_POSITION = Position.Position(cls.LABY.index(line), line.index(x))
					return


	@classmethod
	def initGame(cls):
		cls.loadLABY()
		cls.AVAILABLE_CASES = cls.buildAvailPositionList()
		cls.generateInGameObjets()
		cls.PERSO_INIT_POSITION = Position.Position(0, 1)
		cls.findExitPosition()


	@classmethod
	def updatePersoPositionInLaby(cls, oldPos, newPosition):
		cls.LABY[oldPos.line] = LabyManager.replace(cls.LABY[oldPos.line], oldPos.column, " ")
		cls.LABY[newPosition.line] = LabyManager.replace(cls.LABY[newPosition.line], newPosition.column, "8")


	@classmethod
	def generateInGameObjets(cls):
		for x in xrange(1, 4):
			availableCasesCount = len(cls.AVAILABLE_CASES)
			index = (randint(0, availableCasesCount))
			if index < availableCasesCount:
				position = cls.AVAILABLE_CASES[index]
				if x == 1:
					cls.LABY[position.line] = LabyManager.replace(cls.LABY[position.line], position.column, "A") #A=AIGUILLE
				elif x == 2:
					cls.LABY[position.line] = LabyManager.replace(cls.LABY[position.line], position.column, "E") #E=ETHER
				else:
					cls.LABY[position.line] = LabyManager.replace(cls.LABY[position.line], position.column, "T") #T=TUBE EN PLASTIQUE
				cls.AVAILABLE_CASES.pop(index)

	@classmethod
	def buildAvailPositionList(cls):
		positionList = []
		for line in cls.LABY:
			for x in range(0, len(line)):
				if line[x] == " ":
					indexOfCurrentLine = cls.LABY.index(line)
					positionList.append(Position.Position(indexOfCurrentLine, x))
		return positionList

	@classmethod
	def charAtPosition(cls, pos):
		return cls.LABY[pos.line][pos.column]




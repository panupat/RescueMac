import position as Position
from labyManager import LabyManager

class Perso:
	def __init__(self, pos, hasEther = False, hasTube = False, hasNeedle = False, alive = True):
		self.pos = pos
		self.alive = alive
		self.hasEther = hasEther
		self.hasTube = hasTube
		self.hasNeedle = hasNeedle


	def __str__(self):
		description = "Perso position:\n" + str(self.pos) + "\n"
		description += "alive: " + str(self.alive) + '\n'
		description += "has needle: " + str(self.hasNeedle) + '\n'
		description += "has ether: " + str(self.hasEther) + '\n'
		description += "has tube: " + str(self.hasTube) + '\n'
		return description



	def goLeft(self, laby):
		goingToPos = Position.Position(self.pos.line, self.pos.column - 1)
		self.willStepOnObject(goingToPos)
		if LabyManager.charAtPosition(goingToPos) != "*" and self.pos.column > 0:
			LabyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			LabyManager.showWarning()
    	

	def goRight(self, laby):
		goingToPos = Position.Position(self.pos.line, self.pos.column + 1)
		self.willStepOnObject(goingToPos)
		if LabyManager.charAtPosition(goingToPos) != "*" and self.pos.column < len(laby[self.pos.line]) - 1:
			LabyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			LabyManager.showWarning()
    	

	def goUp(self, laby):
		goingToPos = Position.Position(self.pos.line - 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if LabyManager.charAtPosition(goingToPos) != "*" and self.pos.line > 0:
			LabyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			LabyManager.showWarning()
    	

	def goDown(self, laby):
		goingToPos = Position.Position(self.pos.line + 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if LabyManager.charAtPosition(goingToPos) != "*" and self.pos.line < len(laby) - 1:
			LabyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			LabyManager.showWarning()


	def willStepOnObject(self, pos):
		if LabyManager.charAtPosition(pos) == 'A':
			self.hasNeedle = True
		elif LabyManager.charAtPosition(pos) == 'E':
			self.hasEther = True
		elif LabyManager.charAtPosition(pos) == 'T':
			self.hasTube = True
		elif LabyManager.charAtPosition(pos) == 'X':
			if not self.hasAllObjects():
				self.alive = False


	def hasAllObjects(self):
		return self.hasNeedle and self.hasTube and self.hasEther

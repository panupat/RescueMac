import position as Position
import labyManager as lm

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
		if lm.charAtPosition(goingToPos) != "*" and self.pos.column > 0:
			lm.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			lm.showWarning()
    	

	def goRight(self, laby):
		goingToPos = Position.Position(self.pos.line, self.pos.column + 1)
		self.willStepOnObject(goingToPos)
		if lm.charAtPosition(goingToPos) != "*" and self.pos.column < len(laby[self.pos.line]) - 1:
			lm.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			lm.showWarning()
    	

	def goUp(self, laby):
		goingToPos = Position.Position(self.pos.line - 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if lm.charAtPosition(goingToPos) != "*" and self.pos.line > 0:
			lm.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			lm.showWarning()
    	

	def goDown(self, laby):
		goingToPos = Position.Position(self.pos.line + 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if lm.charAtPosition(goingToPos) != "*" and self.pos.column < len(laby) - 1:
			lm.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			lm.showWarning()


	def willStepOnObject(self, pos):
		if lm.charAtPosition(pos) == 'A':
			self.hasNeedle = True
		elif lm.charAtPosition(pos) == 'E':
			self.hasEther = True
		elif lm.charAtPosition(pos) == 'T':
			self.hasTube = True
		elif lm.charAtPosition(pos) == 'X':
			if not self.hasAllObjects():
				self.alive = False


	def hasAllObjects(self):
		return self.hasNeedle and self.hasTube and self.hasEther

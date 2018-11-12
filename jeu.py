import perso as Perso
import position as Position
import labyManager as lm
from os import system, name
from time import sleep

class GameController:
	LEFTKEY = "a"
	RIGHTKEY = "d"
	UPKEY = "w"
	DOWNKEY = "s"
	SELECTED_KB = "q"

	@staticmethod
	def clear():
		_ = system('clear')


	@staticmethod
	def selectKeyboard():
		print("Appuyez sur Q si vous avez un clavier QWERTY")
		print("Appuyez sur A si vous avez un clavier AZERTY")
		selectedKey = raw_input()
		GameController.setKey(selectedKey)


	@classmethod
	def setKey(cls, selectedKey):
		cls.SELECTED_KB = selectedKey
		if selectedKey == "A" or selectedKey == "a":
			cls.LEFTKEY = "q"
			cls.RIGHTKEY = "d"
			cls.UPKEY = "z"
			cls.DOWNKEY = "s"
			print("Vous avez choisi le clavier AZERTY")
		else:
			print("Vous avez choisi le clavier QWERTY")


	@classmethod
	def explanationString(cls):
		if cls.SELECTED_KB == "A" or cls.SELECTED_KB == "a":
			return "(gauche = q, droite = d, haut = z, bas = s)"
		else:
			return "(left = a, right = d, up = w, down = s)"
		pass

	@classmethod
	def gameLoop(cls, perso):
		win = False
		while (not(perso.pos == lm.exitPosition) and perso.alive):
			lm.displayLaby()
			a = raw_input("ou voulez vous aller: " + cls.explanationString())
			if a == cls.LEFTKEY:
				perso.goLeft(lm.laby)
			elif a == cls.RIGHTKEY:
				perso.goRight(lm.laby)
			elif a == cls.UPKEY:
				perso.goUp(lm.laby)
			elif a == cls.DOWNKEY:
				perso.goDown(lm.laby)
			cls.clear()
		win = perso.alive
		if not win:
			cls.clear()
			print("You are DEAD")
			print("Press enter to continue.")
			_ = raw_input()
		return win


def main():
	gameController = GameController()
	gameController.clear()
	gameController.selectKeyboard()
	sleep(2)
	win = False
	while(not win):
		gameController.clear()
		lm.initGame()
		perso = Perso.Perso(lm.persoInitPosition)
		win = gameController.gameLoop(perso)
	if win:
		lm.displayLaby()
		print("Congrats ! You are out alive !")
		


if __name__ == "__main__":
	main()
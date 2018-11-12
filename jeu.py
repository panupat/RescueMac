import perso as Perso
import position as Position
from labyManager import LabyManager
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
		while (not(perso.pos == LabyManager.EXIT_POSITION) and perso.alive):
			LabyManager.displayLaby()
			a = raw_input("ou voulez vous aller: " + cls.explanationString())
			if a == cls.LEFTKEY:
				perso.goLeft(LabyManager.LABY)
			elif a == cls.RIGHTKEY:
				perso.goRight(LabyManager.LABY)
			elif a == cls.UPKEY:
				perso.goUp(LabyManager.LABY)
			elif a == cls.DOWNKEY:
				perso.goDown(LabyManager.LABY)
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
	labyManager = LabyManager()
	win = False
	while(not win):
		gameController.clear()
		labyManager.initGame()
		perso = Perso.Perso(labyManager.PERSO_INIT_POSITION)
		win = gameController.gameLoop(perso)
	if win:
		labyManager.displayLaby()
		print("Congrats ! You are out alive !")
		


if __name__ == "__main__":
	main()
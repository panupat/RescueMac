import perso as Perso
import position as Position
import labyManager as lm
from os import system, name
from time import sleep

leftKey = "a"
rightKey = "d"
upKey = "w"
downKey = "s"

def clear():
	_ = system('clear')


def selectKeyboard():
	print("Appuyez sur Q si vous avez un clavier QWERTY")
	print("Appuyez sur A si vous avez un clavier AZERTY")
	selectedKey = raw_input()
	setKey(selectedKey)


def setKey(selectedKey):
	if selectedKey == "Q" or selectedKey == "q":
		leftKey = "a"
		rightKey = "d"
		upKey = "w"
		downKey = "s"
		print("Vous avez choisi le clavier QWERTY")
	elif selectedKey == "A" or selectedKey == "a":
		leftKey = "q"
		rightKey = "d"
		upKey = "z"
		downKey = "s"
		print("Vous avez choisi le clavier AZERTY")
	else:
		print("Clavier par defaut selectionne (QWERTY)")

def gameLoop(perso):
	win = False
	while (not(perso.pos == lm.exitPosition) and perso.alive):
		lm.displayLaby()
		a = raw_input("ou voulez vous aller:(gauche = q, droite = d, haut = z, bas = s)")
		if a == leftKey:
			perso.goLeft(lm.laby)
		elif a == rightKey:
			perso.goRight(lm.laby)
		elif a == upKey:
			perso.goUp(lm.laby)
		elif a == downKey:
			perso.goDown(lm.laby)
		clear()
	win = perso.alive
	if not win:
		clear()
		print("You are DEAD")
		print("Press enter to continue.")
		_ = raw_input()
	return win


def main():
	clear()
	selectKeyboard()
	sleep(2)
	win = False
	while(not win):
		clear()
		lm.initGame()
		perso = Perso.Perso(lm.persoInitPosition)
		win = gameLoop(perso)
	if win:
		lm.displayLaby()
		print("Congrats ! You are out alive !")
		


if __name__ == "__main__":
	main()
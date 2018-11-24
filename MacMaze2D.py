import pygame
import position as Position
import perso as Perso
from random import randint
from labyManager import LabyManager
from pygame.locals import *
from constantes import*
from time import sleep


def gameLoop(perso):
    global decision_list
    playloop = True
    win = False
    decision_list = [win, playloop]

    while not (perso.pos == lm.exitPosition) and perso.alive and decision_list[1]:
        #decision_list = [win, playloop]
        lm.displayLaby(shadow)
        pygame.display.set_caption("MacGyver have: " + lm.nbInGameObjets() + "/3 objects. Use arrows to move")
        #lm.message_display("Utilisez les flêches du clavier pour vous déplacer!", shadow)
        pygame.display.flip()
        pygame.key.set_repeat(400,30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                decision_list[1] = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT :
                    perso.goLeft(lm)
                elif event.key == K_RIGHT:
                    perso.goRight(lm)
                elif event.key == K_UP:
                    perso.goUp(lm)
                elif event.key == K_DOWN:
                    perso.goDown(lm)
        decision_list[0] = perso.alive #=TRUE EXCEPT IF GUARD KILL MAC

    if not decision_list[0] and decision_list[1]:
        lm.message_display("You are DEAD, try again!", shadow)
        pygame.display.flip()
        sleep(3)

    elif decision_list[0] and not decision_list[1]:
        lm.message_display("Are you LEAVING?! Tape y or n", shadow)
        pygame.display.flip()
        flag = 1
        while flag:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        decision_list[0] = True
                        decision_list[1] = False
                        lm.displayLaby(shadow)
                        lm.message_display("yes, OK! Thanks", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
                    elif event.key == K_n:
                        decision_list[0] = False
                        decision_list[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("no, OK! Play again", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0

    elif decision_list[0] and decision_list[1]:
        lm.message_display("Mac put it DOWN! Go OUT? Tape y or n", shadow)
        pygame.display.flip()
        flag = 1
        while flag:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        decision_list[0] = True
                        decision_list[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("yes, OK!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
                    elif event.key == K_n:
                        decision_list[0] = False
                        decision_list[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("no, OK!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0

    return decision_list
        

######FONCTION PRINCIPALE##############
pygame.init()
shadow = pygame.display.set_mode((cote_fenetre, cote_fenetre))
playloop = True
win = False
decision_list = [win, playloop]
lm = LabyManager()
while not decision_list[0] and decision_list[1]:
    """Récupération du fichier texte laby nettoyé"""
    lm.initializeGame()
    perso = Perso.Perso(lm.initPosition)
    lm.displayLaby(shadow)
    """affiche l'écran avec les éléments du blit dans l'ordre du code"""
    pygame.display.set_caption('MacGyver Maze')
    pygame.display.flip()
    pygame.key.set_repeat(400,30) 
    win = gameLoop(perso)
if decision_list[0] and decision_list[1]:
    lm.displayLaby(shadow)
    pygame.display.set_caption('MacGyver win')
    lm.message_display("Congrats ! You are out alive !", shadow)
    pygame.display.flip()
    sleep(2)
elif decision_list[0] and not decision_list[1]:
    lm.displayLaby(shadow)
    pygame.display.set_caption('MacGyver win')
    lm.message_display("Thanks for playing! See you soon!", shadow)
    pygame.display.flip()
    sleep(2)

    


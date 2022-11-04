import pygame as pg
import playerCharacter

outOfTurn = [pg.QUIT]


def inTurnAction(playerInput):
    if playerInput in outOfTurn:
        outOfTurnAction(playerInput)
        return True
    else:
        if playerInput == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            playerCharacter.pos = mouse_pos

def outOfTurnAction(playerInput):
    if playerInput == pg.QUIT:
        pg.quit()
        exit()

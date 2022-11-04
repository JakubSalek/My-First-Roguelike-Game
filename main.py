import pygame as pg
import inputControll
import playerCharacter

pg.init()
screen_width = 800
screen_height = 400
screen_size = (screen_width, screen_height)
screen = pg.display.set_mode(screen_size, flags=pg.SCALED)
pg.display.set_caption("University")
gameOn = True
playerTurn = True
player = playerCharacter
player_surface = pg.Surface((10, 10))
player_surface.fill(color='Red')
background_surface = pg.Surface(screen_size)
background_surface.fill(color='Black')

while gameOn:
    if playerTurn:
        for event in pg.event.get():
            playerTurn = inputControll.inTurnAction(event.type)
    else:
        playerTurn = True
    screen.blit(background_surface, (0, 0))
    screen.blit(player_surface, player.pos)
    pg.display.update()

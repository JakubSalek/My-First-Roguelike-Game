import pygame
import SETTINGS
import dungeonMap
import playerCharacter
from GUI import graphicElementsList

pygame.init()
screen_width = SETTINGS.screenWidth
screen_height = SETTINGS.screenHeight
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)
pygame.display.set_caption("University")

clock = pygame.time.Clock()

myDungeonMap = dungeonMap.DungeonMap()
player = playerCharacter.Hero()

background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill('Black')

print(graphicElementsList)

while True:
    screen.blit(background_surface, (0, 0))

    for element in graphicElementsList:
        screen.blit(element.getSurface(), element.getPosition())

    pygame.display.update()

    player.player_movement()
    clock.tick(60)

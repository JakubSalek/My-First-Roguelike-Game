import pygame

import SETTINGS
import playerCharacter
from dungeonMap import dungeonMap, Tile_Type

pygame.init()
screen_width = SETTINGS.screenWidth
screen_height = SETTINGS.screenHeight
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)
pygame.display.set_caption("University")

clock = pygame.time.Clock()

player = playerCharacter.Hero()
player.setPosition(0, 0)

player_surface = pygame.Surface((SETTINGS.tileWidth, SETTINGS.tileHeight))
player_surface.fill('Red')
background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill('Black')
floor_surface = pygame.Surface((SETTINGS.tileWidth, SETTINGS.tileHeight))
floor_surface.fill("Green")
wall_surface = pygame.Surface((SETTINGS.tileWidth, SETTINGS.tileHeight))
wall_surface.fill("Yellow")

while True:
    screen.blit(background_surface, (0, 0))
    for i in range(100):
        for j in range(100):
            if dungeonMap.tileMap[i][j].tileType is Tile_Type.FLOOR:
                screen.blit(floor_surface, (SETTINGS.tileWidth*i, SETTINGS.tileHeight*j))
            elif dungeonMap.tileMap[i][j].tileType is Tile_Type.WALL:
                screen.blit(wall_surface, (SETTINGS.tileWidth*i, SETTINGS.tileHeight*j))
    screen.blit(player_surface, (player.positionX, player.positionY))
    pygame.display.update()

    player.player_movement()
    clock.tick(60)

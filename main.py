import pygame
import dungeonMap
import GUI
import playerCharacter

pygame.init()
screen_width = 1280
screen_height = 720
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)
pygame.display.set_caption("University")

clock = pygame.time.Clock()

dungeon_map = dungeonMap.dungeonMap(screen_width, screen_height)
player = playerCharacter.Hero(0, 0, dungeon_map.tileSizeX, dungeon_map.tileSizeY)

player_surface = pygame.Surface((dungeon_map.tileSizeX, dungeon_map.tileSizeY))
player_surface.fill('Red')
background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill('Black')

while True:
    screen.blit(background_surface, (0, 0))
    screen.blit(player_surface, (player.posX, player.posY))
    pygame.display.update()

    player.player_movement()
    clock.tick(60)

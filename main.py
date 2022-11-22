import pygame

import Game
import SETTINGS

pygame.init()
screen = pygame.display.set_mode((SETTINGS.SCREEN_WIDTH, SETTINGS.SCREEN_HEIGHT), flags=pygame.SCALED)
pygame.display.set_caption("University")

clock = pygame.time.Clock()
Game.GameEngine(screen, clock).startGame()

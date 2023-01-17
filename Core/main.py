import pygame

from Core import Game
import SETTINGS

pygame.init()
screen = pygame.display.set_mode((SETTINGS.SCREEN_WIDTH, SETTINGS.SCREEN_HEIGHT), flags=pygame.SCALED)
pygame.display.set_caption("University")

Game.GameEngine(screen).startGame()

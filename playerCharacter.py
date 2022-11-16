import pygame
import GUI


# Klasa bohatera gry
class Hero:
    def __init__(self, x, y, lrMovLength, udMovLength):
        self.posX = x
        self.posY = y
        self.lrMovLength = lrMovLength
        self.udMovLength = udMovLength
        self.heroTurn = False
        self.inventory = []

    def setHeroTurn(self, heroTurn):
        self.heroTurn = heroTurn

    # Obsługa ruchu gracza
    def player_movement(self):
        self.setHeroTurn(True)
        while self.heroTurn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.posY -= self.udMovLength
                        self.setHeroTurn(False)
                    if event.key == pygame.K_DOWN:
                        self.posY += self.udMovLength
                        self.setHeroTurn(False)
                    if event.key == pygame.K_LEFT:
                        self.posX -= self.lrMovLength
                        self.setHeroTurn(False)
                    if event.key == pygame.K_RIGHT:
                        self.posX += self.lrMovLength
                        self.setHeroTurn(False)

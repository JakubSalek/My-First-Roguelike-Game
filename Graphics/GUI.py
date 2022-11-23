import pygame
import SETTINGS
from Creatures.EnemyType import EnemyType
from Map.TileType import TileType


class GraphicElement:

    def __init__(self):
        self.backgroundGraphic = pygame.Surface(SETTINGS.SCREEN_SIZE)
        self.backgroundGraphic.fill("Black")
        self.emptyTile = pygame.Surface(SETTINGS.TILE_SIZE)
        self.emptyTile.fill("Black")
        self.playerGraphic = pygame.image.load("Graphics/Assets/hero.png").convert_alpha()
        self.ratGraphic = pygame.image.load("Graphics/Assets/rat.png")
        self.wallGraphic = self.surface = pygame.image.load("Graphics/Assets/wall.png")
        self.floorGraphic = self.surface = pygame.image.load("Graphics/Assets/floor.png")

    def getBackGround(self):
        return self.backgroundGraphic

    def getTileGraphics(self, tileType):
        if tileType is TileType.FLOOR:
            return self.floorGraphic
        elif tileType is TileType.WALL:
            return self.wallGraphic
        else:
            return self.emptyTile

    def getEnemyGraphics(self, enemyType):
        if enemyType is EnemyType.RAT:
            return self.ratGraphic

    def printMap(self, screen, dungeonMap, creatures):
        screen.blit(self.getBackGround(), (0, 0))
        heroPosX, heroPosY = creatures[0].getPosition()
        for i in range(SETTINGS.TILES_IN_COL):
            for j in range(SETTINGS.TILES_IN_ROW):
                screen.blit(self.getTileGraphics(dungeonMap[heroPosY - 11 + i][heroPosX - 20 + j].tileType),
                            (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT))
        counter = 0
        for creature in creatures:
            if counter == 0:
                screen.blit(self.playerGraphic,
                            (20 * SETTINGS.TILE_WIDTH, 11 * SETTINGS.TILE_HEIGHT))
                counter += 1
            else:
                creaturePosX, creaturePosY = creature.getPosition()
                screen.blit(self.getEnemyGraphics(creature.enemyType),
                            (creaturePosX * SETTINGS.TILE_WIDTH, creaturePosY * SETTINGS.TILE_HEIGHT))

        pygame.display.update()

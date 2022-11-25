import pygame
import SETTINGS
from Creatures.ActorType import ActorType
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
        elif tileType is TileType.STAIR_DOWN:
            return self.ratGraphic
        elif tileType is TileType.STAIRS_UP:
            return self.playerGraphic
        else:
            return self.emptyTile

    def getEnemyGraphics(self, actorType):
        if actorType is ActorType.PLAYER:
            return self.playerGraphic
        elif actorType is ActorType.RAT:
            return self.ratGraphic
        else:
            return None

    def printMap(self, screen, dungeonMap, creatures):
        screen.blit(self.getBackGround(), (0, 0))
        heroPosX, heroPosY = creatures[0].getPosition()
        for i in range(SETTINGS.TILES_IN_COL):
            for j in range(SETTINGS.TILES_IN_ROW):
                screen.blit(self.getTileGraphics(dungeonMap[heroPosY - 11 + i][heroPosX - 20 + j].tileType),
                            (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT))
                creatureOnTile = self.getEnemyGraphics(dungeonMap[heroPosY - 11 + i][heroPosX - 20 + j].getCreature())
                if creatureOnTile is not None:
                    screen.blit(creatureOnTile, (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT))

        pygame.display.update()

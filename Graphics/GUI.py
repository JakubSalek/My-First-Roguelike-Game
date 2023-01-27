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
        self.wallGraphic = pygame.image.load("Graphics/Assets/wall.png")
        self.floorGraphic = pygame.image.load("Graphics/Assets/floor.png")
        self.stairsDownGraphic = pygame.image.load("Graphics/Assets/stairs_down.png")
        self.stairsUpGraphic = pygame.image.load("Graphics/Assets/stairs_up.png")
        # Character Info
        self.characterInfoBG = pygame.Surface((230, 145))
        self.characterInfoBG.fill("DARKGREY")
        self.healthBarBG = pygame.Surface((200, 50))
        self.expBarBG = pygame.Surface((200, 50))

    def getBackGround(self):
        return self.backgroundGraphic

    def getTileGraphics(self, tileType):
        if tileType is TileType.FLOOR:
            return self.floorGraphic
        elif tileType is TileType.WALL:
            return self.wallGraphic
        elif tileType is TileType.STAIR_DOWN:
            return self.stairsDownGraphic
        elif tileType is TileType.STAIRS_UP:
            return self.stairsUpGraphic
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
                screen.blit(self.getTileGraphics(dungeonMap[heroPosY - int(SETTINGS.TILES_IN_COL / 2) + i] \
                                                     [heroPosX - int(SETTINGS.TILES_IN_ROW / 2) + j].tileType),
                            (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT))
                creatureOnTile = dungeonMap[heroPosY - int(SETTINGS.TILES_IN_COL / 2) + i] \
                    [heroPosX - int(SETTINGS.TILES_IN_ROW / 2) + j].getCreature()
                if creatureOnTile is not None:
                    graphicsOfCreature = self.getEnemyGraphics(creatureOnTile.actorType)
                    screen.blit(graphicsOfCreature, (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT))
                    if creatureOnTile.actorType != ActorType.PLAYER:
                        creatureHealthX = creatureOnTile.stats.currentHealth / creatureOnTile.stats.maxHealth
                        if not 64 * creatureHealthX < 0:
                            healthBar = pygame.Surface((64 * creatureHealthX, 5))
                            healthBar.fill("CRIMSON")
                            screen.blit(healthBar, (j * SETTINGS.TILE_WIDTH, i * SETTINGS.TILE_HEIGHT + 59))

    def printCharacterInfo(self, screen, hero):
        screen.blit(self.characterInfoBG, (0, 0))
        screen.blit(self.healthBarBG, (15, 15))
        screen.blit(self.expBarBG, (15, 80))
        hpPrecent = (hero.stats.currentHealth / hero.stats.maxHealth)
        XPPrecent = (hero.stats.currentExperience / hero.stats.maxExperience)
        currentHPBar = pygame.Surface((hpPrecent * 200, 50))
        currentHPBar.fill("CRIMSON")
        screen.blit(currentHPBar, (15, 15))
        currentXPBar = pygame.Surface((XPPrecent * 200, 50))
        currentXPBar.fill("GREEN")
        screen.blit(currentXPBar, (15, 80))

        pygame.display.update()

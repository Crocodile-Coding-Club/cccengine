from cccengine.renderer.tile import Tile
import pygame

class Chunk:
    def __init__(self, x, y, tiles, textures: list):
        self.x = x
        self.y = y
        self.textures = textures
        self.tiles = self.loadTiles(tiles)
        
    def loadTiles(self, tiles):
        newTiles = pygame.sprite.Group()
        for tile in tiles:
            tile = tile.split("#")
            isEntity = bool(int(tile[5]))
            # id layer collison x y entity colkey
            if isEntity == False:
                newTiles.add(Tile(int(tile[0]), self.textures[int(tile[0])], int(tile[3])*16+320*self.x, int(tile[4])*16+320*self.y, int(tile[1]), int(tile[2]), (int(tile[6]), int(tile[7]), int(tile[8]))))
        return newTiles
    
    def update(self, x, y):
        self.tiles.update(-x, -y)
        
    def draw(self, screen):
        self.tiles.draw(surface=screen)
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        id,
        texture,
        x: int,
        y: int,
        layer: int,
        collision: bool,
        colkey: tuple,
    ):
        super().__init__()
        self.id = id
        self.image: pygame.surface.Surface = pygame.image.load(texture).convert()
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.x = x
        self.y = y
        
        self.rect.topleft = (x, y)

        self.layer = layer
        self.collision = collision
        self.colkey = colkey
        if colkey[0] < 256 and colkey[1] < 256 and colkey[2] < 256:
            self.image.set_colorkey(colkey)
        
    def getLayer(self):
        return self.layer
    
    def update(self, x, y):
        x, y = self.x + x, self.y + y
        self.rect.topleft = (x, y)
import pygame


class Gui(pygame.sprite.Sprite):
    def __init__(self, imagePath, x, y, width, height, position: str = "topleft"):
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        if position == "center":
            self.rect.center(x, y)
        elif position == "topleft":
            self.rect.topleft(x, y)
        elif position == "topright":
            self.rect.topright(x, y)
        elif position == "bottomleft":
            self.rect.bottomleft(x, y)
        elif position == "bottomright":
            self.rect.bottomright(x, y)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        clickType = pygame.mouse.get_pressed()

        if any(clickType):
            self.clicked(clickType)

    def clicked(self, clickType):
        pass

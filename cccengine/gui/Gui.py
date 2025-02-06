import pygame

class BackgroundImage(pygame.sprite.Sprite):
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


class Gui:
    def __init__(self, screen, backgroundImagePath, x, y, width, height, buttons: list[Button], position: str = "topleft"):
        self.backgroundImage = BackgroundImage(backgroundImagePath, x, y, width, height, position)
        self.rect = self.image.get_rect()
        self.buttons = pygame.sprite.Group()
        for button in buttons:
            self.buttons.add(button)

    def update(self):
       self.buttons.update()

    def open(self):
        pass
    
    def display(self):
        self.backgroundImage.draw(self.screen)
        self.buttons.draw(self.screen)
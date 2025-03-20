import pygame
from cccengine.gui.Gui import Gui
from cccengine.events.ButtonClickEvent import ButtonClickEvent


class Button(pygame.sprite.Sprite):
    def __init__(self, gui, imagePath, x, y, width, height, position: str = "topleft"):
        self.gui: "Gui" = gui
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        if position == "center":
            self.rect.center = (x, y)
        elif position == "topleft":
            self.rect.topleft = (x, y)
        elif position == "topright":
            self.rect.topright = (x, y)
        elif position == "bottomleft":
            self.rect.bottomleft = (x, y)
        elif position == "bottomright":
            self.rect.bottomright = (x, y)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        clicks = pygame.mouse.get_pressed()

        if any(clicks):
            if self.rect.collidepoint(mousePos):
                ButtonClickEvent(self, clicks)

    def clicked(self, clicks):
        pass

    def getGui(self):
        return self.gui
import pygame
import cccengine.gui.Gui as Gui
from cccengine.events.ButtonClickEvent import ButtonClickEvent


class Button(pygame.sprite.Sprite):
    def __init__(self, gui, imagePath, x, y, position: str = "topleft"):
        pygame.sprite.Sprite.__init__(self)
        self.gui: "Gui.Gui" = gui
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        self.eventHandler = gui.getEventHandler()

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
        
        gui.buttons.add(self)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        clicks = pygame.mouse.get_pressed()

        if any(clicks):
            if self.rect.collidepoint(mousePos):
                ButtonClickEvent(self.eventHandler, self, clicks)

    def clicked(self, clicks):
        pass

    def getGui(self):
        return self.gui

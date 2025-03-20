import pygame
import cccengine.gui.Button

class BackgroundImage(pygame.sprite.Sprite):
    def __init__(self, image: pygame.surface.Surface, x, y, width, height, position: str = "topleft"):
        super().__init__()
        self.image = image
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


class Gui:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        backgroundImage: BackgroundImage,
        x: int,
        y: int,
        width: int,
        height: int,
        buttons: list["cccengine.gui.Button.Button"] = None,
        position: str = "topleft",
    ):
        self.screen: pygame.surface.Surface = screen
        self.backgroundImage = backgroundImage
        self.buttons = pygame.sprite.Group()
        if buttons != None:
            for button in buttons:
                self.buttons.add(button)

    def update(self):
        self.buttons.update()

    def draw(self):
        self.screen.blit(self.backgroundImage.image, self.backgroundImage.rect)
        # self.buttons.draw(surface=self.surface)

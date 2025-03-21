import pygame
import cccengine.gui.Button as Button


class BackgroundImage(pygame.sprite.Sprite):
    def __init__(
        self,
        image: pygame.surface.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
        position: str = "topleft",
    ):
        super().__init__()
        self.image: pygame.surface.Surface = image
        self.rect: pygame.rect.Rect = self.image.get_rect()

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
        buttons: list["Button.Button"] = [],
        position: str = "topleft",
    ):
        self.screen: pygame.surface.Surface = screen
        self.backgroundImage: BackgroundImage = backgroundImage
        self.buttons: pygame.sprite.Group = pygame.sprite.Group()
        for button in buttons:
            self.buttons.add(button)

    def update(self):
        self.buttons.update()

    def draw(self):
        self.screen.blit(self.backgroundImage.image, self.backgroundImage.rect)
        # self.buttons.draw(surface=self.surface)

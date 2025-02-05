import pygame
from cccengine.events.Event import Event


class SoundPlayEvent(Event):
    """
    SoundPlayEvent Class
    """

    def __init__(self, sound: pygame.mixer.Sound):
        """
        Initialize a SoundPlayEvent instance
        """
        assert (
            type(sound) == pygame.mixer.Sound
        ), "[Error]: sound must be a pygame.mixer.Sound instance"

        super().__init__()

        self.event_name = "Sound Play Event"
        self.sound = sound

    def getSound(self):
        """
        Get the sound of the event
        """
        return self.sound

    def execute(self):
        if self.cancel == False:
            self.sound.play()

import pygame

from cccengine.events.EventHandler import EventHandler
from cccengine.events.SoundPlayEvent import SoundPlayEvent


class AudioManager:
    def __init__(self, backgroundMusic: pygame.mixer.Sound, eventHandler: EventHandler):
        self.soundList: list[pygame.mixer.Sound] = None
        self.backgroundMusic: pygame.mixer.Sound = backgroundMusic
        self.eventHandler = eventHandler

    def addSound(self, sound: pygame.mixer.Sound):
        self.soundList.append(sound)

    def removeSound(self, index: int):
        if len(self.soundList) < index:
            return self.soundList.pop(index)
        return None

    def setMusic(self, music: pygame.mixer.Sound):
        self.backgroundMusic = music

    def playSounds(self):
        for sound in self.soundList:
            event = SoundPlayEvent(sound)
            self.eventHandler.addEvent(event)

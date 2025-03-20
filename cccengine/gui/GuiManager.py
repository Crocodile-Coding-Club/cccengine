from cccengine.gui.Gui import Gui
from cccengine.events.GuiOpenEvent import GuiOpenEvent

class GuiManager:
    def __init__(self, screen, guis: list[Gui] = []):
        self.screen = screen
        self.guis = guis

    def update(self):
       for gui in self.guis:
           gui.update()
    
    def draw(self):
        for gui in self.guis:
            gui.draw()

    def openGui(self, gui):
        GuiOpenEvent(self, gui).execute()

class CommonTextTypes():
    VAL_NYELV = 0
    NYELV = 1
    IRANYITAS = 2

class GameModes():
    RPG = 0
    CYBERSPACE = 1
    WORKSHOP = 2
    HACKING = 3
    MENU = 4

class Languages():
    HU = 0
    EN = 1
    ROV = 2

class Colors():
    
    def __init__(self):
        return
    
    def getBackgroundColor(self, gameMode):
        if gameMode == GameModes.RPG:
            return (255,255,255)
        if gameMode == GameModes.MENU:
            return (255,255,255)
    
    def getForegroundColor(self, gameMode):
        if gameMode == GameModes.RPG:
            return (100,100,100)
        if gameMode == GameModes.MENU:
            return (100,100,100)
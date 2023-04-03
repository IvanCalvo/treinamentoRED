class Ball:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    def setXPos(self, valor):
        self.xPos = valor
    
    def setYPos(self, valor):
        self.yPos = valor
    
    def getXPos(self):
        return self.xPos
    
    def getYPos(self):
        return self.yPos
    
    def setPose(self, x, y):
        self.xPos = x
        self.yPos = y
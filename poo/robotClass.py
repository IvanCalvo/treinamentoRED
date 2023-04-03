class Robot:
    def __init__(self, L = 7.5, R = 3.5):
        self.xPos = 0
        self.yPos = 0
        self.theta = 0
        self.L = L
        self.R = R
    
    def setXPos(self, valor):
        self.xPos = valor

    def setYPos(self, valor):
        self.yPos = valor

    def setTheta(self, valor):
        self.theta = valor

    def setL(self, valor):
        self.L = valor

    def setR(self, valor):
        self.R = valor

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos
    
    def getTheta(self):
        return self.theta
    
    def getL(self):
        return self.L
    
    def getR(self):
        return self.R
    
    def setPose(self, x, y, theta):
        self.xPos = x
        self.yPos = y
        self.theta = theta
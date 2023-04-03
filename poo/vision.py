import numpy as np

class Vision:
    def getPoseRobot():
        x = np.random.uniform(0,150)
        y = np.random.uniform(0,130)
        theta = np.random.uniform(-np.pi, np.pi)
        return x, y, theta
    def getPoseBall():
        x = np.random.uniform(0,150)
        y = np.random.uniform(0,130)
        return x, y
    
print(Vision.getPoseBall())
print(Vision.getPoseRobot())
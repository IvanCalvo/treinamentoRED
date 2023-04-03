import math
import numpy as np

def rotate(X, angulo):
    R = np.matrix([[math.cos(angulo), -math.sin(angulo)], 
                   [math.sin(angulo), math.cos(angulo)]])

    return np.dot(R, X)

X = np.array([1,0])
V = np.array(rotate(X, math.pi/3))
print('angulo original: ', math.atan(X[1]/X[0]))
print('angulo final: ', math.atan(V[0][1]/V[0][0]))

###############
##Design the function "findRotMat" to  return 
# 1) rotMat1: a 2D numpy array which indicates the rotation matrix from xyz to XYZ 
# 2) rotMat2: a 2D numpy array which indicates the rotation matrix from XYZ to xyz 
#It is ok to add other functions if you need
###############

import numpy as np
import cv2

def cos_angle(angle):
    return np.cos(np.deg2rad(angle))

def sin_angle(angle):
    return np.sin(np.deg2rad(angle))

def findRotMat(alpha, beta, gamma):
    #......
    rot_1 = np.array([[cos_angle(alpha), -sin_angle(alpha), 0],
                   [sin_angle(alpha), cos_angle(alpha), 0],
                   [0, 0, 1]])
    
    rot_2 = np.array([[1, 0, 0],
                   [0, cos_angle(beta), -sin_angle(beta)],
                   [0, sin_angle(beta), cos_angle(beta)]])
    
    rot_3 = np.array([[cos_angle(gamma), -sin_angle(gamma), 0],
                   [sin_angle(gamma), cos_angle(gamma), 0],
                   [0, 0, 1]])

    rotMat1 = np.dot(rot_3,(np.dot(rot_2, rot_1)))
    rotMat2 = rotMat1.transpose()
    
    return rotMat1, rotMat2
    
if __name__ == "__main__":
    alpha = 45
    beta = 30
    gamma = 60
    rotMat1, rotMat2 = findRotMat(alpha, beta, gamma)
    print(rotMat1)
    print(rotMat2)

import numpy as np

class Tool:

    def __init__(self, name, pos, quat, cog, orient, moi):
        self.name = name
        self.pos = pos
        self.quat = quat
        self.cog = cog
        self.orient = orient
        self.moi = moi
        self.rotated = self.toRotationMatrix()

    def __str__(self):
        toolStr = ("Name: " + str(self.name) + "\n" +
              "Position: " + str(self.pos) + "\n" +
              "Quaternation " + str(self.quat) + "\n" +
              "Center Of Gravity: " + str(self.cog) + "\n" +
              "Moment Of Inertia: " + str(self.moi) + "\n")
        return toolStr

    def toRotationMatrix(self):
        qa = np.array(self.quat, float)
        norm = np.sqrt(sum(np.square(qa)))
        qa = qa / norm
        
        r = np.zeros((3,3))
        r[0][0] = 1 - 2 * (np.square(qa[2]) + np.square(qa[3]))
        r[0][1] = 2 * (qa[1] * qa[2] - qa[0] * qa[3])
        r[0][2] = 2 * (qa[1] * qa[3] + qa[0] * qa[2])
        r[1][0] = 2 * (qa[1] * qa[2] + qa[0] * qa[3])
        r[1][1] = 1 - 2 * (np.square(qa[1]) + np.square(qa[3]))
        r[1][2] = 2 * (qa[2] * qa[3] - qa[0] * qa[1])
        r[2][0] = 2 * (qa[1] * qa[3] - qa[0] * qa[2])
        r[2][1] = 2 * (qa[2] * qa[3] + qa[0] * qa[1])
        r[2][2] = 1 - 2 * (np.square(qa[1]) + np.square(qa[2]))    

        return r

    def multiply(self, r, v):
        return np.dot(r,v)


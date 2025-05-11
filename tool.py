import numpy as np

class Tool:

    def __init__(self, name, mounted, pos, quat, cog, orient, moi):
        self.name = name
        self.mounted = mounted
        self.pos = pos
        self.quat = quat
        self.cog = cog
        self.orient = orient
        self.moi = moi
        self.rotated = self.toRotationMatrix()

    def __str__(self):
        toolStr = ("Name: " + str(self.name) + "\n" +
                   "Mounted: " + str(self.mounted) + "\n" +
                   "Position: " + str(self.pos) + "\n" +
                   "Quaternation " + str(self.quat) + "\n" +
                   "Center Of Gravity: " + str(self.cog) + "\n" +
                   "COG Orient: " + str(self.orient) + "\n" +
                   "Moment Of Inertia: " + str(self.moi))
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

    def displaceTool(self, coord):
        newPos = self.multiply(self.rotated, coord)
        self.pos[0] = float(newPos[0] + self.pos[0])
        self.pos[1] = float(newPos[1] + self.pos[1])
        self.pos[2] = float(newPos[2] + self.pos[2])

    def displaceWorld(self, coord):
        self.pos[0] = coord[0] + self.pos[0]
        self.pos[1] = coord[1] + self.pos[1]
        self.pos[2] = coord[2] + self.pos[2]
        

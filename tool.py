import numpy as np

#Class to create a Tool object
class Tool:
    #Constructor expects arguments in format (string, string, float[], float[],
    #                                         float[], float[], float[])
    #Mass is expected to be the first value in the cog array
    def __init__(self, name, mounted, pos, quat, cog, orient, moi):
        self.name = name
        self.mounted = mounted
        self.pos = pos
        self.quat = quat
        self.cog = cog
        self.orient = orient
        self.moi = moi
        self.rotated = self.toRotationMatrix()

    #__str__() method creates a string from a Tool object
    def __str__(self):
        #Initialize arrays for values rounded to 6 decimal places
        roundPos = []
        roundQuat = []
        #Round mass and cog values seperate to make formating easyier
        roundMass = round(self.cog[0])
        roundCog = [round(self.cog[1], 6), round(self.cog[2], 6), round(self.cog[3], 6)]
        roundOrient = []
        roundMoi = []

        #Loop through each parameter and append rounded value to array
        for item in self.pos:
            roundPos.append(round(item, 6))
        for item in self.quat:
            roundQuat.append(round(item, 6))
        for item in self.orient:
            roundOrient.append(round(item, 6))
        for item in self.moi:
            roundMoi.append(round(item, 6))

        #Create string from rounded data and format as ABB tooldata line
        toolStr = ("PERS tooldata " + str(self.name) + ":=[" + str(self.mounted) + ",[" +
                   str(roundPos).replace(" ", "") + "," + str(roundQuat).replace(" ", "") +
                   "],[" + str(roundMass) + "," + str(roundCog).replace(" ", "") + "," +
                   str(roundOrient).replace(" ", "") + "," + str(roundMoi[0]) + "," +
                   str(roundMoi[1]) + "," + str(roundMoi[2]) +  "]];")
        return toolStr

    #toRotationMatrix() method creates a rotation matrix
    #from a quaternation array
    def toRotationMatrix(self):
        #Normalize the quaternation
        qa = np.array(self.quat, float)
        norm = np.sqrt(sum(np.square(qa)))
        qa = qa / norm
        #Create and return rotation matrix
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

    #multiply() a rotation matrix by a vectory
    #Must pass a rotation matrix as a two demensional array
    #and a vector as a single deminsonal array
    def multiply(self, r, v):
        return np.dot(r,v)

    #displaceTool() method adjustes the postion array of the
    #tool object by the tool frame.
    #Must pass a 3x1 float[] as an argument
    def displaceTool(self, coord):
        newPos = self.multiply(self.rotated, coord)
        self.pos[0] = float(newPos[0] + self.pos[0])
        self.pos[1] = float(newPos[1] + self.pos[1])
        self.pos[2] = float(newPos[2] + self.pos[2])

    #displaceWorld() method adjustes the postion array of the
    #tool object by the world frame.
    #Must pass a 3x1 float[] as an argument
    def displaceWorld(self, coord):
        self.pos[0] = coord[0] + self.pos[0]
        self.pos[1] = coord[1] + self.pos[1]
        self.pos[2] = coord[2] + self.pos[2]
        

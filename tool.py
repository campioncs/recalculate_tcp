"""Tool module contains classes for working with robot tools.
"""
import numpy as np

class Tool:
    """Tool creates an object from tooldata"""
    def __init__(self, name, mounted, pos, quat, cog, orient, moi):
        """Initializes the tool instance from tooldata

        Args:
          name:
            Name of tool as a string.
          mounted:
            Is the tool mounted to the robot as string "TRUE" or "FALSE".
          pos:
            3 item array of floats containg x, y, and z values for the tool.
          quat:
            4 item array of floats containg the quaternation for the tool.
          cog:
            4 iterm array of floats containing mass as item[0], and
            center of gravity x, y, and z for items[1-3].
          orient:
            4 item array of floats containing quaternation for tool rotation.
          moi:
            3 item array of floats containing moments of intertia
            for x, y, and z.
        """
        self.name = name
        self.mounted = mounted
        self.pos = pos
        self.quat = quat
        self.cog = cog
        self.orient = orient
        self.moi = moi
        self.rotated = self.to_rotation_matrix()

    def __str__(self):
        """Creates a string from a tool object in format of abb tooldata.

        Returns:
          A string in format of abb tooldata.
        """
        #Create arrays for values rounded to 6 decimal places
        round_pos = []
        round_quat = []
        #Round mass and cog values seperate to make formating easyier
        round_mass = round(self.cog[0])
        round_cog = [round(self.cog[1], 6), round(self.cog[2], 6), round(self.cog[3], 6)]
        round_orient = []
        round_moi = []

        #Loop through each parameter and append rounded value to array
        for item in self.pos:
            round_pos.append(round(item, 6))
        for item in self.quat:
            round_quat.append(round(item, 6))
        for item in self.orient:
            round_orient.append(round(item, 6))
        for item in self.moi:
            round_moi.append(round(item, 6))

        #Create string from rounded data and format as ABB tooldata line
        tool_string = ("PERS tooldata " + str(self.name) + ":=[" + str(self.mounted) + ",[" +
                   str(round_pos).replace(" ", "") + "," + str(round_quat).replace(" ", "") +
                   "],[" + str(round_mass) + "," + str(round_cog).replace(" ", "") + "," +
                   str(round_orient).replace(" ", "") + "," + str(round_moi[0]) + "," +
                   str(round_moi[1]) + "," + str(round_moi[2]) +  "]];")
        return tool_string

    def to_rotation_matrix(self):
        """Creates a rotation matrix from a tool quaternation.

        Returns:
           A rotation matrix in form of 2 dimensional array.
        """
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

    def multiply(self, r, v):
        """Multiplies a matrix by a vector.

        Args:
          r:
            Rotation matrix.
          v:
            vector.
        
          Returns:
            resuls of multiplying r by v.
        """
        return np.dot(r,v)

    def displace_tool(self, coord):
        """Mutates tool position by the tool frame.

        Args:
          coord:
            3 item array of floats x, y, and z coordinates to displace tool by.
        """
        new_pos = self.multiply(self.rotated, coord)
        self.pos[0] = float(new_pos[0] + self.pos[0])
        self.pos[1] = float(new_pos[1] + self.pos[1])
        self.pos[2] = float(new_pos[2] + self.pos[2])

    def displace_world(self, coord):
        """Mutates tool position by the world frame.

        Args:
          coord:
            3 item array of floats x, y, and z coordinates to displace world by.
        """
        self.pos[0] = coord[0] + self.pos[0]
        self.pos[1] = coord[1] + self.pos[1]
        self.pos[2] = coord[2] + self.pos[2]

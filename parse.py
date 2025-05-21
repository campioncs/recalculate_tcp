""" Parse module contains classes for parsing tool data."""
class ToolParse:
    """Class to parse tooldata from an abb config file"""
    def __init__(self, f):
        """Initilizes a ToolParse object.
        
        Args:
          f:
            File path to parse.
        """
        self.f = f
        #Array of all lines in file f
        self.lineArray = []
        self.toArray(self.f)
        #Array of lines containing tool data
        self.toolLines = []
        self.locateTool(self.lineArray)
        #Array of dictionaries one dictionary for each tool
        self.dictArray = []
        self.splitTool(self.toolLines)

    def toArray(self, f):
        """Opens file f and creates an array of lines.

        Args:
          f:
            File path to open.
        """
        with open(f) as f:
            for line in f:
                self.lineArray.append(line)

    def locateTool(self, line_array):
        """Locates tooldata lines from array.

        Args:
          line_array:
            Array of lines to locate tooldata from.
        """
        for line in line_array:
            if line.strip().startswith("PERS tooldata") and line.strip().endswith(";"):
                self.toolLines.append(line)

    def splitTool(self, raw_tools):
        """Takes an array of lines with tooldata and splits them into a dictionary.

        Args:
          raw_tools:
            array of tooldata lines
        """
        for item in raw_tools:
            toolDict = dict()
            spaceSplit = item.split()
            colonSplit = spaceSplit[2].split(":")
            toolDict["name"] = colonSplit[0]
            commaSplit = colonSplit[1].split(",")
            toolDict["mounted"] = commaSplit[0].strip("=[")
            toolDict["x"] = commaSplit[1].strip("[")
            toolDict["y"] = commaSplit[2]
            toolDict["z"] = commaSplit[3].strip("]")
            toolDict["q1"] = commaSplit[4].strip("[")
            toolDict["q2"] = commaSplit[5]
            toolDict["q3"] = commaSplit[6]
            toolDict["q4"] = commaSplit[7].strip("]")
            toolDict["mass"] = commaSplit[8].strip("[")
            toolDict["cogX"] = commaSplit[9].strip("[")
            toolDict["cogY"] = commaSplit[10]
            toolDict["cogZ"] = commaSplit[11].strip("]")
            toolDict["orientQ1"] = commaSplit[12].strip("[")
            toolDict["orientQ2"] = commaSplit[13]
            toolDict["orientQ3"] = commaSplit[14]
            toolDict["orientQ4"] = commaSplit[15].strip("]")
            toolDict["moiX"] = commaSplit[16]
            toolDict["moiY"] = commaSplit[17]
            toolDict["moiZ"] = commaSplit[18].strip("]];")
            #Append dictionary to self.dict_array
            self.dictArray.append(toolDict)

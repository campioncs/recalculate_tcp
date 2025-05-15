#Class to parse tool data from an ABB config file
class ToolParse:

    #Constructor needs a file path argument passed to it
    def __init__(self, f):
        #File path
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

    #toArray() method creates an array of lines
    #Must pass file path as argument 
    def toArray(self, f):
        with open(f) as f:
            for line in f:
                self.lineArray.append(line)

    #locateTool() method finds lines containing tooldata
    #Must pass an array of lines
    def locateTool(self, lineArray):
        for line in lineArray:
            if line.strip().startswith("PERS tooldata") and line.strip().endswith(";"):
                self.toolLines.append(line)

    #splitTool() method takes a tooldata line and splits it into a dictionary
    #Must pass an array of lines containing tooldata
    #Appends resulting dictionary to self.dictArray
    def splitTool(self, rawTools):
        for item in rawTools:
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
            self.dictArray.append(toolDict)

class ToolParse:

    def __init__(self, f):
        self.f = f
        self.lineArray = []
        self.toArray(self.f)
        self.toolLines = []
        self.locateTool(self.lineArray)
        self.dictArray = []
        self.splitTool(self.toolLines)

    def toArray(self, f):
        with open(f) as f:
            for line in f:
                self.lineArray.append(line)

    def locateTool(self, lineArray):
        for line in lineArray:
            if line.strip().startswith("PERS tooldata") and line.strip().endswith(";"):
                self.toolLines.append(line)

    def splitTool(self, rawTools):
        for item in rawTools:
            toolDict = dict()
            spaceSplit = item.split()
            colonSplit = spaceSplit[2].split(":")
            name = colonSplit[0]
            commaSplit = colonSplit[1].split(",")
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

    

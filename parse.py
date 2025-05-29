""" Parse module contains classes for parsing tool data."""
class AbbToolParse:
    """Class to parse tooldata from an abb config file"""
    def __init__(self, f):
        """Initilizes a ToolParse object.
        
        Args:
          f:
            File path to parse.
        """
        self.f = f
        #Array of all lines in file f
        self.line_array = self.to_array(self.f)
        #Array of lines containing tool data
        self.tool_lines = self.locate_tool(self.line_array)
        #Array of dictionaries one dictionary for each tool
        self.dict_array = self.split_tool(self.tool_lines)

    def to_array(self, f_path):
        """Opens file f_path and creates an array of lines.

        Args:
          f_path:
            File path to open.

        Returns:
          Array of every line in file f.
        """
        la = []
        with open(f_path, encoding="utf-8") as f:
            for line in f:
                la.append(line)
        return la

    def locate_tool(self, line_array):
        """Locates tooldata lines from array.

        Args:
          line_array:
            Array of lines to locate tooldata from.

        Returns:
          Array of all line from line_array that contains tooldata.
        """
        tl = []
        for line in line_array:
            if line.strip().startswith("PERS tooldata") and line.strip().endswith(";"):
               tl.append(line)
        return tl

    def split_tool(self, raw_tools):
        """Takes an array of lines with tooldata and splits them into a dictionary.

        Args:
          raw_tools:
            array of tooldata lines

        Returns:
          Array of dictionaries containing tooldata by name.
        """
        ta = []
        for item in raw_tools:
            tool_dict = {}
            space_split = item.split()
            colon_split = space_split[2].split(":")
            tool_dict["name"] = colon_split[0]
            comma_split = colon_split[1].split(",")
            tool_dict["mounted"] = comma_split[0].strip("=[")
            tool_dict["x"] = comma_split[1].strip("[")
            tool_dict["y"] = comma_split[2]
            tool_dict["z"] = comma_split[3].strip("]")
            tool_dict["q1"] = comma_split[4].strip("[")
            tool_dict["q2"] = comma_split[5]
            tool_dict["q3"] = comma_split[6]
            tool_dict["q4"] = comma_split[7].strip("]")
            tool_dict["mass"] = comma_split[8].strip("[")
            tool_dict["cogX"] = comma_split[9].strip("[")
            tool_dict["cogY"] = comma_split[10]
            tool_dict["cogZ"] = comma_split[11].strip("]")
            tool_dict["orientQ1"] = comma_split[12].strip("[")
            tool_dict["orientQ2"] = comma_split[13]
            tool_dict["orientQ3"] = comma_split[14]
            tool_dict["orientQ4"] = comma_split[15].strip("]")
            tool_dict["moiX"] = comma_split[16]
            tool_dict["moiY"] = comma_split[17]
            tool_dict["moiZ"] = comma_split[18].strip("]];")
            #Append dictionary to self.dict_array
            ta.append(tool_dict)
        return ta

"""gui module builds the grphical interface for recalculate_tcp."""
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tool import Tool
from parse import AbbToolParse

class GuiTcp:
    """gui module builds the grphical interface for recalculate_tcp."""
    def __init__(self, root):
        """Initilizes root window and locates all graphical objects.

        Args:
          root:
            Root TK window to add objects too.
        """
        root.title("Recalculate TCP")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #Create inner frames
        dataFrame = ttk.Frame(root, padding="3 3 12 12")
        displaceFrame = ttk.Frame(root, padding="3 3 12 12")
        radioFrame = ttk.Frame(root, padding="3 3 12 12")
        buttonFrame = ttk.Frame(root, padding="3 3 12 12")
        #Grid inner frames
        dataFrame.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=2)
        displaceFrame.grid(column=0, row=1, sticky=(N, W, E, S))
        radioFrame.grid(column=0, row=2, sticky=(N, W, S))
        buttonFrame.grid(column=1, row=1, sticky=(N, W, S), rowspan=2)

        #Data entry Frame
        #Initialize name and postion variables, entry boxes, and labels
        self.name_str = StringVar()
        self.x_str = StringVar()
        self.y_str = StringVar()
        self.z_str = StringVar()
        nameEntry = ttk.Entry(dataFrame, width=9, textvariable=self.name_str)
        x_entry = ttk.Entry(dataFrame, width=9, textvariable=self.x_str)
        y_entry = ttk.Entry(dataFrame, width=9, textvariable=self.y_str)
        z_entry = ttk.Entry(dataFrame, width=9, textvariable=self.z_str)
        nameEntry.grid(column=2, row=1, sticky=(W, E))
        x_entry.grid(column=2, row=2, sticky=(W, E))
        y_entry.grid(column=2, row=3, sticky=(W, E))
        z_entry.grid(column=2, row=4, sticky=(W, E))
        ttk.Label(dataFrame, text="Name:").grid(column=1, row=1, sticky=W)
        ttk.Label(dataFrame, text="X:").grid(column=1, row=2, sticky=W)
        ttk.Label(dataFrame, text="Y:").grid(column=1, row=3, sticky=W)
        ttk.Label(dataFrame, text="Z:").grid(column=1, row=4, sticky=W)

        #Initialize quaternation variables, entry boxes, and labels
        self.q1_str = StringVar()
        self.q2_str = StringVar()
        self.q3_str = StringVar()
        self.q4_str = StringVar()
        q1_entry = ttk.Entry(dataFrame, width=9, textvariable=self.q1_str)
        q2_entry = ttk.Entry(dataFrame, width=9, textvariable=self.q2_str)
        q3_entry = ttk.Entry(dataFrame, width=9, textvariable=self.q3_str)
        q4_entry = ttk.Entry(dataFrame, width=9, textvariable=self.q4_str)
        q1_entry.grid(column=4, row=1, sticky=(E, W))
        q2_entry.grid(column=4, row=2, sticky=(E, W))
        q3_entry.grid(column=4, row=3, sticky=(E, W))
        q4_entry.grid(column=4, row=4, sticky=(E, W))
        ttk.Label(dataFrame, text="q1:").grid(column=3, row=1, sticky=W)
        ttk.Label(dataFrame, text="q2:").grid(column=3, row=2, sticky=W)
        ttk.Label(dataFrame, text="q3:").grid(column=3, row=3, sticky=W)
        ttk.Label(dataFrame, text="q4:").grid(column=3, row=4, sticky=W)

        #Initialize mass and center of gravity variables, entry boxes, and labels
        self.mass_str = StringVar()
        self.cog_x_str = StringVar()
        self.cog_y_str = StringVar()
        self.cog_z_str = StringVar()
        mass_entry = ttk.Entry(dataFrame, width=9, textvariable=self.mass_str)
        cog_x_entry = ttk.Entry(dataFrame, width=9, textvariable=self.cog_x_str)
        cog_y_entry = ttk.Entry(dataFrame, width=9, textvariable=self.cog_y_str)
        cog_z_entry = ttk.Entry(dataFrame, width=9, textvariable=self.cog_z_str)
        mass_entry.grid(column=6, row=1, sticky=(E, W))
        cog_x_entry.grid(column=6, row=2, sticky=(E, W))
        cog_y_entry.grid(column=6, row=3, sticky=(E, W))
        cog_z_entry.grid(column=6, row=4, sticky=(E, W))
        ttk.Label(dataFrame, text="Mass:").grid(column=5, row=1, sticky=W)
        ttk.Label(dataFrame, text="cogX:").grid(column=5, row=2, sticky=W)
        ttk.Label(dataFrame, text="cogY:").grid(column=5, row=3, sticky=W)
        ttk.Label(dataFrame, text="cogZ:").grid(column=5, row=4, sticky=W)

        #Initialize orientation quaternation variables, entry boxes, and labels
        self.orient_q1_str = StringVar()
        self.orient_q2_str = StringVar()
        self.orient_q3_str = StringVar()
        self.orient_q4_str = StringVar()
        orient_q1_entry = ttk.Entry(dataFrame, width=9, textvariable=self.orient_q1_str)
        orient_q2_entry = ttk.Entry(dataFrame, width=9, textvariable=self.orient_q2_str)
        orient_q3_entry = ttk.Entry(dataFrame, width=9, textvariable=self.orient_q3_str)
        orient_q4_entry = ttk.Entry(dataFrame, width=9, textvariable=self.orient_q4_str)
        orient_q1_entry.grid(column=8, row=1, sticky=(W, E))
        orient_q2_entry.grid(column=8, row=2, sticky=(W, E))
        orient_q3_entry.grid(column=8, row=3, sticky=(W, E))
        orient_q4_entry.grid(column=8, row=4, sticky=(W, E))
        ttk.Label(dataFrame, text="Orient Q1:").grid(column=7, row=1, sticky=W)
        ttk.Label(dataFrame, text="Orient Q2:").grid(column=7, row=2, sticky=W)
        ttk.Label(dataFrame, text="Orient Q3:").grid(column=7, row=3, sticky=W)
        ttk.Label(dataFrame, text="Orient Q4:").grid(column=7, row=4, sticky=W)

        #Initialize moment of inertia variables, entry boxes, and labels
        self.moiXStr = StringVar()
        self.moiYStr = StringVar()
        self.moiZStr = StringVar()
        moiXEntry = ttk.Entry(dataFrame, width=9, textvariable=self.moiXStr)
        moiYEntry = ttk.Entry(dataFrame, width=9, textvariable=self.moiYStr)
        moiZEntry = ttk.Entry(dataFrame, width=9, textvariable=self.moiZStr)
        moiXEntry.grid(column=10,row=1, sticky=(W, E))
        moiYEntry.grid(column=10,row=2, sticky=(W, E))
        moiZEntry.grid(column=10,row=3, sticky=(W, E))
        ttk.Label(dataFrame, text="moiX:").grid(column=9, row=1, sticky=W)
        ttk.Label(dataFrame, text="moiY:").grid(column=9, row=2, sticky=W)
        ttk.Label(dataFrame, text="moiZ:").grid(column=9, row=3, sticky=W)

        #Displacement value entry frame
        #Initialize displacement variables, entry boxes, and labels
        self.dispXStr = StringVar(value="0")
        self.dispYStr = StringVar(value="0")
        self.dispZStr = StringVar(value="0")
        dispXEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispXStr)
        dispYEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispYStr)
        dispZEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispZStr)
        dispXEntry.grid(column=2, row=2, sticky=(W, E))
        dispYEntry.grid(column=4, row=2, sticky=(W, E))
        dispZEntry.grid(column=6, row=2, sticky=(W, E))
        ttk.Label(displaceFrame, text="Displacement Values:",
                  font=("Helvetica", 12, "bold")).grid(column=1, row=1, columnspan=4, sticky=W)
        ttk.Label(displaceFrame, text="X:").grid(column=1, row=2, sticky=W)
        ttk.Label(displaceFrame, text="Y:").grid(column=3, row=2, sticky=W)
        ttk.Label(displaceFrame, text="Z:").grid(column=5, row=2, sticky=W)

        #Radio button frame
        #Is tool mounted to the robot TRUE/FALSE
        self.mountedStr = StringVar()
        radT = ttk.Radiobutton(radioFrame, text="TRUE",
                               variable=self.mountedStr, value="TRUE")
        radF = ttk.Radiobutton(radioFrame, text="FALSE",
                               variable=self.mountedStr, value="FALSE")
        ttk.Label(radioFrame, text="Is tool mounted:",
                  font=("Helvetica", 8, "bold")).grid(column=1, row=1, sticky=W)
        radT.grid(column=2, row=1, sticky=W)
        radF.grid(column=2, row=2, sticky=W)
        self.mountedStr.set("TRUE")

        #Operating on Tool frame, or World frame
        self.frameStr = StringVar()
        radTool = ttk.Radiobutton(radioFrame, text="Tool",
                                  variable=self.frameStr, value="tool")
        radWorld = ttk.Radiobutton(radioFrame, text="World",
                                   variable=self.frameStr, value="world")
        ttk.Label(radioFrame, text="Select frame:",
                  font=("Helvetica", 8, "bold")).grid(column=3, row=1, sticky=W)
        radTool.grid(column=4, row=1, sticky=W)
        radWorld.grid(column=4, row=2, sticky=W)
        self.frameStr.set("tool")

        #Button frame
        ttk.Button(buttonFrame, text="Load tool from file",
                   command=self.loadTool).grid(column=1, row=1, sticky=(S, W))
        ttk.Button(buttonFrame, text="Save to file",
                   command=self.rootSaveFile).grid(column=1, row=2, sticky=(S, W))
        ttk.Button(buttonFrame, text="Save to new file",
                   command=self.rootSaveAsFile).grid(column=1, row=3, sticky=(S, W))
        ttk.Button(buttonFrame, text="Calculate",
                   command=self.calculate).grid(column=2, row=1, sticky=(S, W), rowspan=3)

        #Loop through all frames, bind enter to calculate, and set padding
        for child in dataFrame.winfo_children():
            child.grid_configure(padx=5, pady=5)
            x_entry.focus()
            root.bind("<Return>", self.calculate)
        for child in displaceFrame.winfo_children():
            child.grid_configure(padx=5)
            root.bind("<Return>", self.calculate)
        for child in radioFrame.winfo_children():
            root.bind("<Return>", self.calculate)
        for child in buttonFrame.winfo_children():
            child.grid_configure(padx=3, pady=5)
            root.bind("<Return>", self.calculate)

    def calculate(self, event=None):
        """Creates a top level window and presents the results of calculation."""
        #Get displacement values as string.
        #Convert them to floating point numbers, and create array
        dispVector = [float(self.dispXStr.get()), float(self.dispYStr.get()),
                      float(self.dispZStr.get())]
        #Using the Tool class, create tool object from entered values
        calcTool = self.createTool()
        if self.frameStr.get() == "tool":
            calcTool.displace_tool(dispVector)
        else:
            calcTool.displace_world(dispVector)

        #Display results in a popup window
        results = Toplevel()
        results.title("Results")
        ttk.Label(results, text=calcTool,
                  font=("Helvetica", 10, "bold")).grid(column=1, row=1, sticky=W,
                                                      columnspan=4, padx=5, pady=5)
        ttk.Button(results, text="Copy to clipboard",
                   command=lambda: self.toClip(results,calcTool)).grid(column=1, row=2,
                                                                       sticky=W, padx=5, pady=5)
        ttk.Button(results, text="Save to File",
                   command=lambda: self.saveFile(calcTool)).grid(column=2, row=2,
                                                              sticky=W, padx=5, pady=5)
        ttk.Button(results, text="Save to new File",
                   command=lambda: self.saveAsFile(calcTool)).grid(column=3, row=2,
                                                              sticky=W, padx=5, pady=5)
        ttk.Button(results, text="Close",
                   command=results.destroy).grid(column=4, row=2,
                                                 sticky=W, padx=5, pady=5)

    def createTool(self):
        """Creates a tool object from entered data.

        Returns:
          Tool object.
        """
        #Convert entered data into floating point numbers
        #ToDo: add error checking
        pos = [float(self.x_str.get()), float(self.y_str.get()), float(self.z_str.get())]
        quat = [float(self.q1_str.get()), float(self.q2_str.get()), float(self.q3_str.get()),
                float(self.q4_str.get())]
        cog = [float(self.mass_str.get()), float(self.cog_x_str.get()),
               float(self.cog_y_str.get()), float(self.cog_z_str.get())]
        orient = [float(self.orient_q1_str.get()), float(self.orient_q2_str.get()),
                  float(self.orient_q3_str.get()), float(self.orient_q4_str.get())]
        moi = [float(self.moiXStr.get()), float(self.moiYStr.get()), float(self.moiZStr.get())]

        #Return tool object
        return  Tool(self.name_str.get(), self.mountedStr.get(), pos, quat, cog, orient, moi)


    def rootSaveFile(self):
        """Save file button for root window when tool object needs to be crated."""
        self.saveFile(self.createTool())

    def rootSaveAsFile(self):
        """Save new file button for root window when tool object needs to be crated."""
        self.saveAsFile(self.createTool())

    def saveFile(self, tool):
        """creates a file dialog to append tool to existing file.

        Args:
          tool:
            Tool object to save.
        """
        saveFilename = filedialog.askopenfilename()
        with open(saveFilename, "a") as f:
            f.write(str(tool) + "\n")
        #Generate popup on success
        messagebox.showinfo("Tool Saved", tool.name + " saved to " + saveFilename)

    def saveAsFile(self, tool):
        """Creates a file dialog to append tool to a new file.

        Args:
          tool:
            Tool object to save.
        """
        saveFilename = filedialog.asksaveasfilename()
        with open(saveFilename, "a") as f:
            f.write(str(tool) + "\n")
        #Generates popup on success
        messagebox.showinfo("Tool Saved", tool.name + " saved to " + saveFilename)

    def toClip(self, window, data):
        """Copies data to clipboard

        Args:
          window:
            TK frame
          data:
            Sting to be copied to clipboard
        """
        window.clipboard_clear()
        window.clipboard_append(data)
        window.update()

    def loadTool(self):
        """Loads a tool from a file, parses tooldata, and fills in all the fields."""
        #Prompt user to select file
        filename = filedialog.askopenfilename()
        #Create AbbToolParseobject from file
        toolData = AbbToolParse(filename)
        #Check if more than one tool was found
        #ToDo: create notice if no tools were wound
        if len(toolData.dict_array) > 1:
            #If more than one tool was found,
            #create a new window for user to select one
            selectTool = Toplevel()
            selectTool.title("Select tool to modify")
            #Create an array of the name of each tool found
            choices = []
            for item in toolData.dict_array:
                choices.append(item["name"])
            #Configure listbox from choices
            choicesVar = StringVar(value=choices)
            #Okay button passes window and chosen tool dictionary
            #to okayPress() method
            okay = ttk.Button(selectTool, text="Okay")
            okay.configure(command=lambda:self.okayPress(selectTool,
                                                         toolData.dict_array[lbox.curselection()[0]]))
            #Grid okay button, and listbox
            okay.grid(column=2, row=1, sticky=(S, E))
            lbox = Listbox(selectTool, listvariable=choicesVar)
            lbox.grid(column=1, row=1, sticky=(N, S, W))
            lbox.activate(0)
            lbox.selection_set(0)
            #Set double click item to invoke okay button
            lbox.bind("<Double-1>", lambda x: okay.invoke())

        else:
            #Else only one tool found
            #Set all data fields from the dictionary
            self.setData(toolData.dict_array[0])

    def setData(self, chosen):
        """Sets all entry boxes from a tool dictionary.

        Args:
          chosen:
           Tool dictonary chosen to enter.
        """
        self.name_str.set(chosen["name"])
        self.mountedStr.set(chosen["mounted"])
        self.x_str.set(chosen["x"])
        self.y_str.set(chosen["y"])
        self.z_str.set(chosen["z"])
        self.q1_str.set(chosen["q1"])
        self.q2_str.set(chosen["q2"])
        self.q3_str.set(chosen["q3"])
        self.q4_str.set(chosen["q4"])
        self.mass_str.set(chosen["mass"])
        self.cog_x_str.set(chosen["cogX"])
        self.cog_y_str.set(chosen["cogY"])
        self.cog_z_str.set(chosen["cogZ"])
        self.orient_q1_str.set(chosen["orientQ1"])
        self.orient_q2_str.set(chosen["orientQ2"])
        self.orient_q3_str.set(chosen["orientQ3"])
        self.orient_q4_str.set(chosen["orientQ4"])
        self.moiXStr.set(chosen["moiX"])
        self.moiYStr.set(chosen["moiY"])
        self.moiZStr.set(chosen["moiZ"])

    def okayPress(self, st, chosen):
        """method to handle okay button from listbox.

        Args:
          st:
            parent window frame.
          chosen:
            tool dictionary chosen from listbox.
        """
        self.setData(chosen)
        #Close parent window
        st.destroy()

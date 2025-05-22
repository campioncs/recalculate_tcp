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
        data_frame = ttk.Frame(root, padding="3 3 12 12")
        displace_frame = ttk.Frame(root, padding="3 3 12 12")
        radio_frame = ttk.Frame(root, padding="3 3 12 12")
        button_frame = ttk.Frame(root, padding="3 3 12 12")
        #Grid inner frames
        data_frame.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=2)
        displace_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        radio_frame.grid(column=0, row=2, sticky=(N, W, S))
        button_frame.grid(column=1, row=1, sticky=(N, W, S), rowspan=2)

        #Data entry Frame
        #Initialize name and postion variables, entry boxes, and labels
        self.name_str = StringVar()
        self.x_str = StringVar()
        self.y_str = StringVar()
        self.z_str = StringVar()
        nameEntry = ttk.Entry(data_frame, width=9, textvariable=self.name_str)
        x_entry = ttk.Entry(data_frame, width=9, textvariable=self.x_str)
        y_entry = ttk.Entry(data_frame, width=9, textvariable=self.y_str)
        z_entry = ttk.Entry(data_frame, width=9, textvariable=self.z_str)
        nameEntry.grid(column=2, row=1, sticky=(W, E))
        x_entry.grid(column=2, row=2, sticky=(W, E))
        y_entry.grid(column=2, row=3, sticky=(W, E))
        z_entry.grid(column=2, row=4, sticky=(W, E))
        ttk.Label(data_frame, text="Name:").grid(column=1, row=1, sticky=W)
        ttk.Label(data_frame, text="X:").grid(column=1, row=2, sticky=W)
        ttk.Label(data_frame, text="Y:").grid(column=1, row=3, sticky=W)
        ttk.Label(data_frame, text="Z:").grid(column=1, row=4, sticky=W)

        #Initialize quaternation variables, entry boxes, and labels
        self.q1_str = StringVar()
        self.q2_str = StringVar()
        self.q3_str = StringVar()
        self.q4_str = StringVar()
        q1_entry = ttk.Entry(data_frame, width=9, textvariable=self.q1_str)
        q2_entry = ttk.Entry(data_frame, width=9, textvariable=self.q2_str)
        q3_entry = ttk.Entry(data_frame, width=9, textvariable=self.q3_str)
        q4_entry = ttk.Entry(data_frame, width=9, textvariable=self.q4_str)
        q1_entry.grid(column=4, row=1, sticky=(E, W))
        q2_entry.grid(column=4, row=2, sticky=(E, W))
        q3_entry.grid(column=4, row=3, sticky=(E, W))
        q4_entry.grid(column=4, row=4, sticky=(E, W))
        ttk.Label(data_frame, text="q1:").grid(column=3, row=1, sticky=W)
        ttk.Label(data_frame, text="q2:").grid(column=3, row=2, sticky=W)
        ttk.Label(data_frame, text="q3:").grid(column=3, row=3, sticky=W)
        ttk.Label(data_frame, text="q4:").grid(column=3, row=4, sticky=W)

        #Initialize mass and center of gravity variables, entry boxes, and labels
        self.mass_str = StringVar()
        self.cog_x_str = StringVar()
        self.cog_y_str = StringVar()
        self.cog_z_str = StringVar()
        mass_entry = ttk.Entry(data_frame, width=9, textvariable=self.mass_str)
        cog_x_entry = ttk.Entry(data_frame, width=9, textvariable=self.cog_x_str)
        cog_y_entry = ttk.Entry(data_frame, width=9, textvariable=self.cog_y_str)
        cog_z_entry = ttk.Entry(data_frame, width=9, textvariable=self.cog_z_str)
        mass_entry.grid(column=6, row=1, sticky=(E, W))
        cog_x_entry.grid(column=6, row=2, sticky=(E, W))
        cog_y_entry.grid(column=6, row=3, sticky=(E, W))
        cog_z_entry.grid(column=6, row=4, sticky=(E, W))
        ttk.Label(data_frame, text="Mass:").grid(column=5, row=1, sticky=W)
        ttk.Label(data_frame, text="cog X:").grid(column=5, row=2, sticky=W)
        ttk.Label(data_frame, text="cog Y:").grid(column=5, row=3, sticky=W)
        ttk.Label(data_frame, text="cog Z:").grid(column=5, row=4, sticky=W)

        #Initialize orientation quaternation variables, entry boxes, and labels
        self.orient_q1_str = StringVar()
        self.orient_q2_str = StringVar()
        self.orient_q3_str = StringVar()
        self.orient_q4_str = StringVar()
        orient_q1_entry = ttk.Entry(data_frame, width=9, textvariable=self.orient_q1_str)
        orient_q2_entry = ttk.Entry(data_frame, width=9, textvariable=self.orient_q2_str)
        orient_q3_entry = ttk.Entry(data_frame, width=9, textvariable=self.orient_q3_str)
        orient_q4_entry = ttk.Entry(data_frame, width=9, textvariable=self.orient_q4_str)
        orient_q1_entry.grid(column=8, row=1, sticky=(W, E))
        orient_q2_entry.grid(column=8, row=2, sticky=(W, E))
        orient_q3_entry.grid(column=8, row=3, sticky=(W, E))
        orient_q4_entry.grid(column=8, row=4, sticky=(W, E))
        ttk.Label(data_frame, text="Orient Q1:").grid(column=7, row=1, sticky=W)
        ttk.Label(data_frame, text="Orient Q2:").grid(column=7, row=2, sticky=W)
        ttk.Label(data_frame, text="Orient Q3:").grid(column=7, row=3, sticky=W)
        ttk.Label(data_frame, text="Orient Q4:").grid(column=7, row=4, sticky=W)

        #Initialize moment of inertia variables, entry boxes, and labels
        self.moi_x_str = StringVar()
        self.moi_y_str = StringVar()
        self.moi_z_str = StringVar()
        moi_x_entry = ttk.Entry(data_frame, width=9, textvariable=self.moi_x_str)
        moi_y_entry = ttk.Entry(data_frame, width=9, textvariable=self.moi_y_str)
        moi_z_entry = ttk.Entry(data_frame, width=9, textvariable=self.moi_z_str)
        moi_x_entry.grid(column=10,row=1, sticky=(W, E))
        moi_y_entry.grid(column=10,row=2, sticky=(W, E))
        moi_z_entry.grid(column=10,row=3, sticky=(W, E))
        ttk.Label(data_frame, text="moi X:").grid(column=9, row=1, sticky=W)
        ttk.Label(data_frame, text="moi Y:").grid(column=9, row=2, sticky=W)
        ttk.Label(data_frame, text="moi Z:").grid(column=9, row=3, sticky=W)

        #Displacement value entry frame
        #Initialize displacement variables, entry boxes, and labels
        self.disp_x_str = StringVar(value="0")
        self.disp_y_str = StringVar(value="0")
        self.disp_z_str = StringVar(value="0")
        disp_x_entry = ttk.Entry(displace_frame, width=9, textvariable=self.disp_x_str)
        disp_y_entry = ttk.Entry(displace_frame, width=9, textvariable=self.disp_y_str)
        disp_z_entry = ttk.Entry(displace_frame, width=9, textvariable=self.disp_z_str)
        disp_x_entry.grid(column=2, row=2, sticky=(W, E))
        disp_y_entry.grid(column=4, row=2, sticky=(W, E))
        disp_z_entry.grid(column=6, row=2, sticky=(W, E))
        ttk.Label(displace_frame, text="Displacement Values:",
                  font=("Helvetica", 12, "bold")).grid(column=1, row=1, columnspan=4, sticky=W)
        ttk.Label(displace_frame, text="X:").grid(column=1, row=2, sticky=W)
        ttk.Label(displace_frame, text="Y:").grid(column=3, row=2, sticky=W)
        ttk.Label(displace_frame, text="Z:").grid(column=5, row=2, sticky=W)

        #Radio button frame
        #Is tool mounted to the robot TRUE/FALSE
        self.mounted_str = StringVar()
        rad_true = ttk.Radiobutton(radio_frame, text="TRUE",
                               variable=self.mounted_str, value="TRUE")
        rad_false = ttk.Radiobutton(radio_frame, text="FALSE",
                               variable=self.mounted_str, value="FALSE")
        ttk.Label(radio_frame, text="Is tool mounted:",
                  font=("Helvetica", 8, "bold")).grid(column=1, row=1, sticky=W)
        rad_true.grid(column=2, row=1, sticky=W)
        rad_false.grid(column=2, row=2, sticky=W)
        self.mounted_str.set("TRUE")

        #Operating on Tool frame, or World frame
        self.frame_str = StringVar()
        rad_tool = ttk.Radiobutton(radio_frame, text="Tool",
                                  variable=self.frame_str, value="tool")
        rad_world = ttk.Radiobutton(radio_frame, text="World",
                                   variable=self.frame_str, value="world")
        ttk.Label(radio_frame, text="Select frame:",
                  font=("Helvetica", 8, "bold")).grid(column=3, row=1, sticky=W)
        rad_tool.grid(column=4, row=1, sticky=W)
        rad_world.grid(column=4, row=2, sticky=W)
        self.frame_str.set("tool")

        #Button frame
        ttk.Button(button_frame, text="Load tool from file",
                   command=self.loadTool).grid(column=1, row=1, sticky=(S, W))
        ttk.Button(button_frame, text="Save to file",
                   command=self.rootSaveFile).grid(column=1, row=2, sticky=(S, W))
        ttk.Button(button_frame, text="Save to new file",
                   command=self.rootSaveAsFile).grid(column=1, row=3, sticky=(S, W))
        ttk.Button(button_frame, text="Calculate",
                   command=self.calculate).grid(column=2, row=1, sticky=(S, W), rowspan=3)

        #Loop through all frames, bind enter to calculate, and set padding
        for child in data_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
            x_entry.focus()
            root.bind("<Return>", self.calculate)
        for child in displace_frame.winfo_children():
            child.grid_configure(padx=5)
            root.bind("<Return>", self.calculate)
        for child in radio_frame.winfo_children():
            root.bind("<Return>", self.calculate)
        for child in button_frame.winfo_children():
            child.grid_configure(padx=3, pady=5)
            root.bind("<Return>", self.calculate)

    def calculate(self, event=None):
        """Creates a top level window and presents the results of calculation."""
        #Get displacement values as string.
        #Convert them to floating point numbers, and create array
        disp_vector = [float(self.disp_x_str.get()), float(self.disp_y_str.get()),
                      float(self.disp_z_str.get())]
        #Using the Tool class, create tool object from entered values
        calc_tool = self.createTool()
        if self.frame_str.get() == "tool":
            calc_tool.displace_tool(disp_vector)
        else:
            calc_tool.displace_world(disp_vector)

        #Display results in a popup window
        results = Toplevel()
        results.title("Results")
        ttk.Label(results, text=calc_tool,
                  font=("Helvetica", 10, "bold")).grid(column=1, row=1, sticky=W,
                                                      columnspan=4, padx=5, pady=5)
        ttk.Button(results, text="Copy to clipboard",
                   command=lambda: self.toClip(results,calc_tool)).grid(column=1, row=2,
                                                                       sticky=W, padx=5, pady=5)
        ttk.Button(results, text="Save to File",
                   command=lambda: self.saveFile(calc_tool)).grid(column=2, row=2,
                                                              sticky=W, padx=5, pady=5)
        ttk.Button(results, text="Save to new File",
                   command=lambda: self.saveAsFile(calc_tool)).grid(column=3, row=2,
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
        moi = [float(self.moi_x_str.get()), float(self.moi_y_str.get()), float(self.moi_z_str.get())]

        #Return tool object
        return  Tool(self.name_str.get(), self.mounted_str.get(), pos, quat, cog, orient, moi)


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
        save_filename = filedialog.askopenfilename()
        with open(save_filename, "a", encoding="utf-8") as f:
            f.write(str(tool) + "\n")
        #Generate popup on success
        messagebox.showinfo("Tool Saved", tool.name + " saved to " + save_filename)

    def saveAsFile(self, tool):
        """Creates a file dialog to append tool to a new file.

        Args:
          tool:
            Tool object to save.
        """
        save_filename = filedialog.asksaveasfilename()
        with open(save_filename, "a", encoding="utf-8") as f:
            f.write(str(tool) + "\n")
        #Generates popup on success
        messagebox.showinfo("Tool Saved", tool.name + " saved to " + save_filename)

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
        tool_data = AbbToolParse(filename)
        #Check if more than one tool was found
        #ToDo: create notice if no tools were wound
        if len(tool_data.dict_array) > 1:
            #If more than one tool was found,
            #create a new window for user to select one
            select_tool = Toplevel()
            select_tool.title("Select tool to modify")
            #Create an array of the name of each tool found
            choices = []
            for item in tool_data.dict_array:
                choices.append(item["name"])
            #Configure listbox from choices
            choices_var = StringVar(value=choices)
            #Okay button passes window and chosen tool dictionary
            #to okayPress() method
            okay = ttk.Button(select_tool, text="Okay")
            okay.configure(command=lambda:self.okayPress(select_tool,
                                                         tool_data.dict_array[lbox.curselection()[0]]))
            #Grid okay button, and listbox
            okay.grid(column=2, row=1, sticky=(S, E))
            lbox = Listbox(select_tool, listvariable=choices_var)
            lbox.grid(column=1, row=1, sticky=(N, S, W))
            lbox.activate(0)
            lbox.selection_set(0)
            #Set double click item to invoke okay button
            lbox.bind("<Double-1>", lambda x: okay.invoke())

        else:
            #Else only one tool found
            #Set all data fields from the dictionary
            self.setData(tool_data.dict_array[0])

    def setData(self, chosen):
        """Sets all entry boxes from a tool dictionary.

        Args:
          chosen:
           Tool dictonary chosen to enter.
        """
        self.name_str.set(chosen["name"])
        self.mounted_str.set(chosen["mounted"])
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
        self.moi_x_str.set(chosen["moiX"])
        self.moi_y_str.set(chosen["moiY"])
        self.moi_z_str.set(chosen["moiZ"])

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

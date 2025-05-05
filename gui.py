from tkinter import *
from tkinter import ttk

class GuiTcp:

    def __init__(self, root):
        
        root.title("Recalculate TCP")

        dataFrame = ttk.Frame(root, padding="3 3 12 12")
        displaceFrame = ttk.Frame(root, padding="3 3 12 12")
        buttonFrame = ttk.Frame(root, padding="3 3 12 12")
        
        dataFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        displaceFrame.grid(column=0, row=1, sticky=(N, W, E, S))
        buttonFrame.grid(column=0, row=2, sticky=(N, W, E, S))
        
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.initialX = StringVar()
        self.initialY = StringVar()
        self.initialZ = StringVar()

        initialXEntry = ttk.Entry(dataFrame, width=9, textvariable=self.initialX)
        initialYEntry = ttk.Entry(dataFrame, width=9, textvariable=self.initialY)
        initialZEntry = ttk.Entry(dataFrame, width=9, textvariable=self.initialZ)

        initialXEntry.grid(column=2, row=1, sticky=(W, E))
        initialYEntry.grid(column=2, row=2, sticky=(W, E))
        initialZEntry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(dataFrame, text="Initial X value:").grid(column=1, row=1, sticky=W)
        ttk.Label(dataFrame, text="Initial Y value:").grid(column=1, row=2, sticky=W)
        ttk.Label(dataFrame, text="Initial Z value:").grid(column=1, row=3, sticky=W)

        self.q1Str = StringVar()
        self.q2Str = StringVar()
        self.q3Str = StringVar()
        self.q2Str = StringVar()

        q1StrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.q1Str)
        q2StrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.q2Str)
        q3StrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.q3Str)
        q4StrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.q3Str)

        q1StrEntry.grid(column=4, row=1, sticky=(E, W))
        q2StrEntry.grid(column=4, row=2, sticky=(E, W))       
        q3StrEntry.grid(column=4, row=3, sticky=(E, W))
        q4StrEntry.grid(column=4, row=4, sticky=(E, W))
        
        ttk.Label(dataFrame, text="q1:").grid(column=3, row=1, sticky=W)
        ttk.Label(dataFrame, text="q2:").grid(column=3, row=2, sticky=W)
        ttk.Label(dataFrame, text="q3:").grid(column=3, row=3, sticky=W)
        ttk.Label(dataFrame, text="q4:").grid(column=3, row=4, sticky=W)

        self.massStr = StringVar()
        self.cogXStr = StringVar()
        self.cogYStr = StringVar()
        self.cogZStr = StringVar()

        massStrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.massStr)
        cogXStrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.cogXStr)
        cogYStrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.cogYStr)
        cogZStrEntry = ttk.Entry(dataFrame, width=9, textvariable=self.cogZStr)
        
        massStrEntry.grid(column=6, row=1, sticky=(E, W))
        cogXStrEntry.grid(column=6, row=2, sticky=(E, W))
        cogYStrEntry.grid(column=6, row=3, sticky=(E, W))
        cogZStrEntry.grid(column=6, row=4, sticky=(E, W))

        ttk.Label(dataFrame, text="Mass:").grid(column=5, row=1, sticky=W)
        ttk.Label(dataFrame, text="cogX:").grid(column=5, row=2, sticky=W)
        ttk.Label(dataFrame, text="cogY:").grid(column=5, row=3, sticky=W)
        ttk.Label(dataFrame, text="cogZ:").grid(column=5, row=4, sticky=W)

        self.cogOrQ1Str = StringVar()
        self.cogOrQ2Str = StringVar()
        self.cogOrQ3Str = StringVar()
        self.cogOrQ4Str = StringVar()

        cogOrQ1Entry = ttk.Entry(dataFrame, width=9, textvariable=self.cogOrQ1Str)
        cogOrQ2Entry = ttk.Entry(dataFrame, width=9, textvariable=self.cogOrQ2Str)
        cogOrQ3Entry = ttk.Entry(dataFrame, width=9, textvariable=self.cogOrQ3Str)
        cogOrQ4Entry = ttk.Entry(dataFrame, width=9, textvariable=self.cogOrQ4Str)

        cogOrQ1Entry.grid(column=8, row=1, sticky=(W, E))
        cogOrQ2Entry.grid(column=8, row=2, sticky=(W, E))
        cogOrQ3Entry.grid(column=8, row=3, sticky=(W, E))
        cogOrQ4Entry.grid(column=8, row=4, sticky=(W, E))

        ttk.Label(dataFrame, text="cogOrient Q1:").grid(column=7, row=1, sticky=W)
        ttk.Label(dataFrame, text="cogOrient Q2:").grid(column=7, row=2, sticky=W)
        ttk.Label(dataFrame, text="cogOrient Q3:").grid(column=7, row=3, sticky=W)
        ttk.Label(dataFrame, text="cogOrient Q4:").grid(column=7, row=4, sticky=W)

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

        self.dispXStr = StringVar()
        self.dispYStr = StringVar()
        self.dispZStr = StringVar()

        dispXEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispXStr)
        dispYEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispYStr)
        dispZEntry = ttk.Entry(displaceFrame, width=9, textvariable=self.dispXStr)

        dispXEntry.grid(column=2, row=2, sticky=(W, E))
        dispYEntry.grid(column=4, row=2, sticky=(W, E))
        dispZEntry.grid(column=6, row=2, sticky=(W, E))

        ttk.Label(displaceFrame, text="Displacement Values:",
                  font=("Helvetica", 12, "bold")).grid(column=1, row=1, columnspan=4, sticky=W)
        ttk.Label(displaceFrame, text="X:").grid(column=1, row=2, sticky=W)
        ttk.Label(displaceFrame, text="Y:").grid(column=3, row=2, sticky=W)
        ttk.Label(displaceFrame, text="Z:").grid(column=5, row=2, sticky=W)

        self.frameStr = StringVar()
        radTool = ttk.Radiobutton(buttonFrame, text="Tool",
                                  variable=self.frameStr, value="tool")
        radWorld = ttk.Radiobutton(buttonFrame, text="World",
                                   variable=self.frameStr, value="world")
        radTool.grid(column=1, row=1, sticky=W)
        radWorld.grid(column=1, row=2, sticky=W)
        self.frameStr.set("tool")
        
        ttk.Button(buttonFrame, text="Load tool from file",
                   command=self.loadTool).grid(column=2, row=1, sticky=W)
        ttk.Button(buttonFrame, text="Save tool to file",
                   command=self.saveTool).grid(column=3, row=1, sticky=W)
        ttk.Button(buttonFrame, text="Calculate",
                   command=self.calculate).grid(column=4, row=1, sticky=(S, E), rowspan=3)

        for child in dataFrame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            initialXEntry.focus()
            root.bind("<Return>", self.calculate)
        for child in displaceFrame.winfo_children():
            child.grid_configure(padx=5)
            root.bind("<Return>", self.calculate)
        for child in buttonFrame.winfo_children():
            child.grid_configure(padx=5)
            root.bind("<Return>", self.calculate)
            
    def calculate(*args):
        pass
    def loadTool():
        pass
    def saveTool():
        pass

root = Tk()
GuiTcp(root)
root.mainloop()

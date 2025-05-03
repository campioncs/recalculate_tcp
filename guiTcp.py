from tkinter import *
from tkinter import ttk

class guiTcp:

    def __init__(self, root):
        
        root.title("Recalculate TCP")

        dataFrame = ttk.Frame(root, padding="3 3 12 12")
        buttonFrame = ttk.Frame(root, padding="3 3 12 12")
        dataFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        buttonFrame.grid(column=0, row=1, sticky=(N, W, E, S))
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


        ttk.Button(buttonFrame, text="Calculate",
                   command=self.calculate).grid(column=1, row=1, sticky=W)

        ttk.Label(dataFrame, text="Initial X value:").grid(column=1, row=1, sticky=W)
        ttk.Label(dataFrame, text="Initial Y value:").grid(column=1, row=2, sticky=W)
        ttk.Label(dataFrame, text="Initial Z value:").grid(column=1, row=3, sticky=W)

        for child in dataFrame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            initialXEntry.focus()
            root.bind("<Return>", self.calculate)

    def calculate(*args):
        try:
            value = float(initialX.get())
            newX.set(value * 10)
        except ValueError:
            pass


root = Tk()
guiTcp(root)
root.mainloop()

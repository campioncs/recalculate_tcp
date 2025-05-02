from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(initialX.get())
        newX.set(value * 10)
    except ValueError:
        pass

root = Tk()
root.title("Recalculate TCP")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

initialX = StringVar()
initialXEntry = ttk.Entry(mainframe, width=7, textvariable=initialX)
initialXEntry.grid(column=2, row=1, sticky=(W, E))

newX = StringVar()
ttk.Label(mainframe, textvariable=newX).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Initial X value").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="New X value is").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    initialXEntry.focus()
    root.bind("<Return>", calculate)

root.mainloop()

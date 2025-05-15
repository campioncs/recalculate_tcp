#Launches recalculate interface
from tkinter import Tk
from gui import GuiTcp
#Create root window
root = Tk()
#Pass root window to GuiTcp class
GuiTcp(root)
#Start event loop
root.mainloop()

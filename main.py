import tkinter as tk
import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
 
root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')
 
label = tk.Label(root, text = "Proyecto de vigilancia")
label.pack(padx = 5, pady = 5)
 
root.mainloop()
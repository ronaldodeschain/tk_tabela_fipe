import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title(' tests with font')
root.minsize(300,200)

#creating new fonts
font1 = Font(
    family='helvetica',
    size=18,
    weight='bold',
    slant='italic',
    underline= True,
    overstrike=False
)

tk.Label(root,text='ola bem vindo ao tkinter',font=font1).pack()


root.mainloop()
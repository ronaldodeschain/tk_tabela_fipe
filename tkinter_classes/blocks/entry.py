import tkinter as tk

root = tk.Tk()
root.title("Entry widget")

label = tk.Label(root,text="Name")
entry = tk.Entry(root)

entry.insert(0,'Placeholder')
# entry.config(state='disabled')\desativa o campo para não ser alterado

label.pack()
entry.pack()


root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title('achor')
root.minsize(300,200)

#how to position elements in a widget
frame = tk.Frame(root).pack()
tk.Label(frame,text='North').pack(anchor='n')
tk.Label(frame,text='Sout').pack(anchor='s')
tk.Label(frame,text='East').pack(anchor='e')
tk.Label(frame,text='West').pack(anchor='w')


root.mainloop()
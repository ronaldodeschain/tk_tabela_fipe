import tkinter as tk

root = tk.Tk()
root.title('spinbox aplications')
root.minsize(300,200)

#form que pode ser incrementado/decrementado ou setado para um valor dentro da
#range
tk.Spinbox(root,from_=0,to=10).pack()

root.mainloop()
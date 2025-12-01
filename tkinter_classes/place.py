import tkinter as tk

root = tk.Tk()
root.title('place')
root.minsize(300,200)

btn = tk.Button(root,text='my place')
#aceita width e height entre outros métodos
btn.place(x=60,y=35)

root.mainloop()
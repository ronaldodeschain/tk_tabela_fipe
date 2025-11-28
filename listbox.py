import tkinter as tk

root = tk.Tk()
root.title('list box')
root.minsize(300,200)

l = tk.Listbox(root,width=10,height=15,justify='right',selectbackground='red',
            selectmode='extended')

for item in range(15):
    l.insert('end',item)

l.pack()
root.mainloop()
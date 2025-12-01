import tkinter as tk

root = tk.Tk()
root.title('scrolling through a list')
root.minsize(300,200)

frame = tk.Frame(root,height=7,width=10)

l = tk.Listbox(frame,width=15,height=15,justify='right',selectbackground='red',
            selectmode='extended')

#alternative config for side scrolling
#scroll = tk.Scrollbar(frame,command=l.xview,orient='horizontal')
scroll = tk.Scrollbar(frame,command=l.yview)
#l.config(xscrollcommand=scroll.set)
l.config(yscrollcommand=scroll.set)

for item in range(20):
    l.insert('end',f"This is a very long line for item {item}")
scroll.pack(side='left',fill='y')
l.pack()
#scroll.pack(side='bottom',fill='x')

frame.pack()
root.mainloop()
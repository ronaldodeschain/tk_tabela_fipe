import tkinter as tk

root = tk.Tk()
root.title('the grid')
root.minsize(300,200)
""" Grid, método para inserir objeto por coluna e linha na aplicação"""
for r in range(4):
    for c in range(4):
        tk.Button(root,text="R%s -- C%s"%(r,c),bg='yellow').grid(row=r,column=c,
                                                    padx=3,pady=2)


root.mainloop()
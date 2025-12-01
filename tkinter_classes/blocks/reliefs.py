import random
import tkinter as tk

root =tk.Tk()
root.title('reliefs')
root.minsize(300,200)

#multiplos estilos de relief para botões. Método para permitir testar todos
def relief():
    rel = ['raised','sunken','flat','groove','ridge']
    if btn['relief'] in rel:
        i = random.randint(0,4)
        btn.config(relief = rel[i]) #type: ignore
        btn.config(text=rel[i])

btn = tk.Button(root,text='Raised',relief='raised',command=relief)
btn.pack()

root.mainloop()
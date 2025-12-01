import tkinter as tk

root = tk.Tk()
root.title('Toplevel widget here')
root.minsize(300,200)

top_level = None

def top():
    global top_level
    top_level = tk.Toplevel(root)
    label = tk.Label(top_level,text='Terms and Conditions =D ').pack()
    terms = tk.Message(top_level,text='this is an agreement that you will' \
    'rock the world with us really hard',width=100).pack()
    #botão radio que aparece no top level
    radio = tk.Radiobutton(top_level,text='By your command',command=agree,
                        state='normal',value=1).pack()
    radio = tk.Radiobutton(top_level,text='Nay, that wont do',command=root.quit,
                        state='normal').pack()
    
def agree(): #comando para seguir com aplicação apos confirmar
    global top_level
    tk.Label(root,text='Welcome to the Brotherhood of Steel').pack()
    top_level.destroy() #type:ignore

btn = tk.Button(root,text='Install',command=top).pack()

root.mainloop()
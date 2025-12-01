import random
import tkinter as tk

root = tk.Tk()
root.title('Cursors')
root.minsize(300,200)

#método para ciclar entre os cursores disponiveis no tkinter
def on_click():
    cursors = ['arrow','circle','clock','cross','dotbox','exchange',
        'fleur','heart','man','mouse']
    if btn['cursor'] in cursors:
        i = random.randint(0,len(cursors)-1)
        btn.config(cursor=cursors[i])
        label.config(text=cursors[i].upper())

label = tk.Label(root,text='ARROW')
btn = tk.Button(root,text='Raised',relief='raised',cursor='arrow',command=on_click)

btn.pack()
label.pack()
root.mainloop()
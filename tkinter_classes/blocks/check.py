import tkinter as tk

root = tk.Tk()
root.title('Checkbutton widget')
root.minsize(300,200)

palavra = {'nome','outronome','novonome','nonome','saindo'}
tk.Label(root,text='select your selection').pack()
for palavra in palavra:
    chkbtn = tk.Checkbutton(root,text=f'{palavra}').pack()
    



root.mainloop()
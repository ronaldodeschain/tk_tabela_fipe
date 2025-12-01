import random
import tkinter as tk

root = tk.Tk()
root.title('bitmaps')
root.minsize(300,200)

#metodo para ciclar entre os bitmaps disponiveis no tkinter
def on_click():
    bmp = ['error','gray25','gray50','gray75','gray12','hourglass',
        'questhead','info','warning','question']
    if btn['bitmap'] in bmp:
        i = random.randint(0,len(bmp)-1)
        btn.config(bitmap=bmp[i])
        label.config(text=bmp[i].upper())

label = tk.Label(root,text='ERROR')
btn = tk.Button(root,text='Raised',relief='raised',bitmap='error',command=on_click)

btn.pack()
label.pack()
root.mainloop()
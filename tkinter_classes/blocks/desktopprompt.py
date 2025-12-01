import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Messagebox: Desktop prompts')
root.minsize(300,200)

def show_info():
    messagebox.showinfo('Info','Not all who glitter are gold')

def show_warning():
    messagebox.showwarning('Notice','Senhor dos aneis é o melhor filme')

def show_error():
    messagebox.showerror('Mistake','I noticed that you are noticing me')

def show_question():
    answer = messagebox.askquestion('Info', 'Voce concorda que é o melhor?')
    if answer == 'yes':
        tk.Label(root,text='Welcome Brother').pack()
    else:
        tk.Label(root,text='Ainda dá tempo de mudar de ideia').pack()

btn_info = tk.Button(root,text='Click Info',command=show_info).pack()
btn_warning = tk.Button(root,text='Click Warning',command=show_warning).pack()
btn_error = tk.Button(root,text='Click Error',command=show_error).pack()
btn_question = tk.Button(root,text='Click Question',command=show_question).pack()

root.mainloop()
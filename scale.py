import tkinter as tk

root = tk.Tk()
root.title('Scale like thermometer')
root.minsize(300,200)

def scale_color(value):
    if(int(value) <= 20):
        scale.config(bg='green')
    elif(20 <int(value) <= 40):
        scale.config(bg='yellow')
    elif(40 < int(value) <=65):
        scale.config(bg='orange')
    else:
        scale.config(bg='red')

scale = tk.Scale(root,length=250,from_=0,to=100,tickinterval=15,
                 orient='horizontal',command=scale_color)
scale.set(30)

scale.pack()

root.mainloop()
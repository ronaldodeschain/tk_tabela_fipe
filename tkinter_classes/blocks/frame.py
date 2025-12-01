import tkinter as tk

root = tk.Tk()
root.title("Frames")
root.minsize(300,200)

frame = tk.Frame(root,bg='lightblue',height=400,width=400)

label = tk.Label(frame,text='um texto de frame',bg='lightgreen',font='arial',wraplength=300).pack()

for text,value in [('Apple',1),('Banana',2),('grape',3),('Cheese',4)]:
    tk.Radiobutton(frame,text=text,value=value,indicatoron=0,width=20).pack() #type:ignore

frame.pack()
root.mainloop()
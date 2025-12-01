import tkinter as tk

root = tk.Tk()
root.title("Radio")
root.minsize(300,200)

for text,value in [('Apple',1),('Banana',2),('grape',3),('Cheese',4)]:
    tk.Radiobutton(root,text=text,value=value,indicatoron=0).pack() #type:ignore


root.mainloop()



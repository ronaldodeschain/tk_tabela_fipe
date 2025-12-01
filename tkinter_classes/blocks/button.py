import tkinter as tk

root = tk.Tk()
root.title("Botão widget")

btn = tk.Button(root,text="click clickit clackt",relief='raised').pack()
# btn = tk.Button(root,text="click clickit clackt",relief='sunken').pack()
# btn = tk.Button(root,text="click clickit clackt",relief='flat').pack()
# btn = tk.Button(root,text="click clickit clackt",relief='ridge').pack()
# btn = tk.Button(root,text="click clickit clackt",relief='groove').pack()
# btn = tk.Button(root,text="click clickit clackt",relief='solid').pack()


root.mainloop()
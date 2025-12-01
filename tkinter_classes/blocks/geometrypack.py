import tkinter as tk

root = tk.Tk()
root.title('Pack method geometry manager')
root.minsize(300,200)

#.pack()
#.grid() - Best for position on the application
#.place()

tk.Button(root,text="default position").pack()
tk.Button(root,text="default position atributes").pack(side='top',
                                                    anchor='center',fill='none'
                                                    ,expand=0)
tk.Button(root,text="default position atributes").pack(side='bottom',
                                                    anchor='sw',fill='x'
                                                    ,expand=1)

root.mainloop()
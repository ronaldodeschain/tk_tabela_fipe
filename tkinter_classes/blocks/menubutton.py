import tkinter as tk

root = tk.Tk()
root.minsize(300,200)
root.title('Menu with menubutton')

#cria um menu que expande a partir de um botão
menu_button = tk.Menubutton(root,text='select options')

menu = tk.Menu(menu_button,tearoff=False)
menu_button['menu'] = menu
menu.add_command(label='Option 1')
menu.add_command(label='Option 2')
menu.add_command(label='Option 3')
menu.add_command(label='Option 4')

menu_button.pack()

root.mainloop()
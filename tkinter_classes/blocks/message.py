import tkinter as tk

root = tk.Tk()
root.title('message widget')
root.minsize(300,200)

tk.Label(root,text='Nos podemos dizer que o message widget é igual ao label' \
' só que ele mostra textos longos em multiplas linhas, é um tipo de modo obsoleto' \
'mas que pode ajudar em alguns casos',bg='red').pack()

tk.Message(root,text='podemos dizer que o message widget é igual ao label' \
' só que ele mostra textos longos em multiplas linhas, é um tipo de modo obsoleto' \
'mas que pode ajudar em ' \
'alguns casos',bg='royalblue',width=200,justify='center',relief='raised').pack()

root.mainloop()
import tkinter as tk

"""
Exemplo de alterações nas dimensões do texto usando width
"""
root = tk.Tk()
root.title('dimensions')
root.minsize(300,200)

#width - centimeters
tk.Message(root,text='Lorem consequat anim est esse et aliqua Lorem ' \
'anim incididunt cupidatat culpa laborum sunt ullamco. ' \
'In ullamco eu dolore irure ullamco magna qui laborum consequat eiusmod sit' \
' veniam est. Adipisicing id ipsum anim fugiat ullamco et culpa laborum ' \
'exercitation est sunt esse eiusmod. Duis ex magna occaecat exercitation ' \
'labore. Culpa nostrud magna pariatur irure qui deserunt anim ad excepteur' \
' labore nostrud Lorem esse laboris. Minim enim sunt ea elit velit Lorem ' \
'nisi pariatur.',width='5c').pack()

#width = inches
tk.Message(root,text='Lorem consequat anim est esse et aliqua Lorem ' \
'anim incididunt cupidatat culpa laborum sunt ullamco. ' \
'In ullamco eu dolore irure ullamco magna qui laborum consequat eiusmod sit' \
' veniam est. Adipisicing id ipsum anim fugiat ullamco et culpa laborum ' \
'exercitation est sunt esse eiusmod. Duis ex magna occaecat exercitation ' \
'labore. Culpa nostrud magna pariatur irure qui deserunt anim ad excepteur' \
' labore nostrud Lorem esse laboris. Minim enim sunt ea elit velit Lorem ' \
'nisi pariatur.',width='5i').pack()

#width = milimeters
tk.Message(root,text='Lorem consequat anim est esse et aliqua Lorem ' \
'anim incididunt cupidatat culpa laborum sunt ullamco. ' \
'In ullamco eu dolore irure ullamco magna qui laborum consequat eiusmod sit' \
' veniam est. Adipisicing id ipsum anim fugiat ullamco et culpa laborum ' \
'exercitation est sunt esse eiusmod. Duis ex magna occaecat exercitation ' \
'labore. Culpa nostrud magna pariatur irure qui deserunt anim ad excepteur' \
' labore nostrud Lorem esse laboris. Minim enim sunt ea elit velit Lorem ' \
'nisi pariatur.',width='5m').pack()

root.mainloop()
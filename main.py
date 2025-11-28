import tkinter as tk
from tkinter import ttk

app = tk.Tk()

#pegar dimensões da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

#passando o padding percentual
pad_x_percent = 0.3
pad_y_percent = 0.3

#convertendo em pixels
pad_x = int(largura_tela * pad_x_percent)
pad_y = int(altura_tela * pad_y_percent)

def clicou(name):
    print(f"clicou {name}")


tela = ttk.Frame(app, padding=(pad_x,pad_y))
tela.grid()


ttk.Label(tela, text="Hello World!").grid(column=0, row=0)
ttk.Button(tela,text="clique me",command=lambda: clicou("Marilene")).grid(column=1, row=0)
ttk.Button(tela, text="Quit", command=app.destroy).grid(column=1, row=1)
app.mainloop()
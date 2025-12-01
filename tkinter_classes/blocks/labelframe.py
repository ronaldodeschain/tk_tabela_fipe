import tkinter as tk

root = tk.Tk()
root.title('label frame')
root.minsize(300,200)

#criando frames para campos de formulário
label_frame = tk.LabelFrame(root,text='Login')
label_frame.pack()

#definindo os campos do formulário
label_email = tk.Label(label_frame,text='Email: ')
email_entry = tk.Entry(label_frame)
label_password = tk.Label(label_frame,text='Password: ')
password_entry = tk.Entry(label_frame)

#posicionando os campos criados dentro do formulário
label_email.grid(column=0,row=0)
email_entry.grid(column=1,row=0)
label_password.grid(column=0,row=1)
password_entry.grid(column=1,row=1)

root.mainloop()
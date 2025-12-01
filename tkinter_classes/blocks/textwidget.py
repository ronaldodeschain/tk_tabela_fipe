import tkinter as tk
from PIL import Image,ImageTk

image = Image.open('vault.jpg')
image = image.resize((200,200))

root = tk.Tk()
root.title('text widget')
root.minsize(300,200)

img = ImageTk.PhotoImage(image)

text = tk.Text(root)
text.insert("insert",'Not all who wander are lost\n')
text.insert("end",'Not all that glitters are gold')
text.image_create("end",image=img)

text.pack()

text.tag_add('here','1.0','1.35')
text.tag_add('next','2.0','2.36')
text.tag_config('here',background='orange',font='times')
text.tag_config('next',background='lightblue',font='colibri')



root.mainloop()
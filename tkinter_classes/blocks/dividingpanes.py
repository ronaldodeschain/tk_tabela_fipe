import tkinter as tk

root = tk.Tk()
root.title('dividing with panes')
root.minsize(300,200)

#orient = 'vertical' to change the orientation of the panes
panewindow = tk.PanedWindow(root,bg='yellow',orient='vertical',width=200,height=50)

panewindow.pack()

l1 = tk.Label(panewindow,text='Pane 1')
panewindow.add(l1)
l2 = tk.Label(panewindow,text='Pane 2')
panewindow.add(l2)
l3 = tk.Label(panewindow,text='Panel 3')
panewindow.add(l3)

root.mainloop()
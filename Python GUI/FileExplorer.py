import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def OpenFile():
    out = filedialog.askopenfilename()
    pic = Image.open(out)
    a,b = pic.size
    ratio = b/a
    pic_resized = pic.resize((250,int(250*(ratio))), Image.Resampling.NEAREST)
    new_pic = ImageTk.PhotoImage(pic_resized)
    img_label.configure(image= new_pic)
    img_label.image = new_pic

def exit_func(event):
    v = list_var.get()
    if v == item[1]:
        exit()
    
window = ttk.Window()
window.title('File Explorer')
window.geometry('550x600')

button = ttk.Button(window, text= 'Open File Explorer', command= OpenFile)
button.pack()

exit_button = ttk.Button(window, text= 'Exit', command= lambda: exit())
exit_button.pack(pady= 10)

img_label = ttk.Label(window)
img_label.pack(pady= 10)

item = ('Do Nothing', 'Exit')
list_var = tk.StringVar(value = item[0])
combobox = ttk.Combobox(window, textvariable= list_var)
combobox['values'] = item
combobox.bind('<FocusIn>', exit_func)
combobox.pack()


window.mainloop()

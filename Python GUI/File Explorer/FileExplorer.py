import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from PIL import Image, ImageTk

#definitions
def OpenFile(): #opens the file and resizes it
    directory = filedialog.askopenfilename(
        initialdir= "C:\\Users\\DELL\\OneDrive\\Pictures\\POSTERS", 
        filetypes= (("jpeg files", "*.jpg"),("png files", "*.png"))
        )
    pic = Image.open(directory)
    h,w = pic.size
    ratio = w/h
    pic_resized = pic.resize((450,int(450*(ratio))), Image.Resampling.NEAREST)
    resized_pic = ImageTk.PhotoImage(pic_resized)
    img_label.configure(image= resized_pic)
    img_label.image = resized_pic

def exit_func(event): #closes the window when exit is selected
    v = list_var.get()
    if v == item[1]:
        exit()

#window    
window = ttk.Window(themename= 'solar')
window.title('Image Displayer')
window.geometry('550x700')

#button frame starts
frame = ttk.Frame()

#buttons
open_button = ttk.Button(
    frame, 
    text= 'Open File Explorer', 
    command= OpenFile
    )
open_button.pack(pady= 5, padx= 3)
open_button.pack(side= 'left')

exit_button = ttk.Button(
    frame, 
    text= 'Exit', 
    command= lambda: exit()
    )
exit_button.pack(side= 'left')

frame.pack() 
#button frame ends

#image
img_label = ttk.Label(window)
img_label.pack(expand = True)
img_label.pack(pady= 10)

#combobox
item = ('Do Nothing', 'Exit')
list_var = tk.StringVar(value = item[0])
combobox = ttk.Combobox(window, textvariable= list_var)
combobox['values'] = item
combobox.bind('<FocusIn>', exit_func)
combobox.pack()

#run
window.mainloop()

# end
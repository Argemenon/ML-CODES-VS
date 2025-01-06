import tkinter as tk
# from tkinter import ttk
from PIL import ImageTk, Image
import ttkbootstrap as ttk
# import ttk
import numpy as np
import time

def DisplayTime():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    time_var.set(f'Time: {curr_time}')
    window.after(10, DisplayTime)

def Rad():
    deg_input = entry_Int.get()
    rad_output = deg_input * (np.pi/180)
    rad_output =  '{0:.3f}'.format(rad_output)
    output_string.set(f'{rad_output} Rad')

def Deg():
    rad_input = entry_Int.get()
    deg_output = rad_input * (180/np.pi)
    deg_output =  '{0:.3f}'.format(deg_output)
    output_string.set(f'{deg_output} °')

#Window

window =ttk.Window(themename= 'solar')
window.title("Angle Converter")
window.geometry("550x350")

# Title Frame
title_frame = ttk.Frame(window)

#title
title_value = tk.StringVar(value= 'Degrees to Radians')
title_label = ttk.Label(
    master = title_frame,
    textvariable= title_value,
    font='Candara 30')
title_label.pack(side= 'right')

#Photo
pic = Image.open('Python GUI\\Unit Converter\\logo.png')

pic_resized = pic.resize((70,70), Image.Resampling.NEAREST)

new_pic = ImageTk.PhotoImage(pic_resized)

img_label = ttk.Label(title_frame, image = new_pic)
img_label.pack(side= 'right')

title_frame.pack()
title_frame.pack(pady=20)

#radio
radio_value = tk.BooleanVar(value= True)

radio1 = ttk.Radiobutton(
    window, 
    text='Degrees to Radians', 
    value= True, 
    command= lambda: title_value.set(value= 'Degrees to Radians'), 
    variable= radio_value)
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text='Radians to Degrees', 
    value= False, 
    command= lambda: title_value.set(value= 'Radians to Degrees'),
    variable= radio_value)
radio2.pack()

# function
def convert():
    if radio_value.get() is False:
        return(Deg())
    else:
        return(Rad())
        

#input field
input_frame = ttk.Frame(master=window)

entry_Int = tk.DoubleVar()

entry = ttk.Entry(master=input_frame, textvariable= entry_Int, font='Candara 15')

button = ttk.Button(master= input_frame, text='Convert', command = convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = "Output",
    font = 'Candara 24',
    textvariable = output_string,
    foreground= 'yellow')
output_label.pack(pady=5)

#time
time_var = tk.StringVar(value = 'time')
tim = ttk.Label(window, textvariable= time_var,font = 'Candara 15')
tim.pack(side= 'left')
tim.pack(padx=10)
DisplayTime()

#run
window.mainloop()
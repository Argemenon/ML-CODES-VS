import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
# import ttk
import numpy as np

def convert():
    deg_input = entry_Int.get()
    rad_output = deg_input * (np.pi/180)
    output_string.set(rad_output)

#Window

window =ttk.Window(themename= 'darkly')
window.title("Degrees to Radians")
window.geometry("500x200")

#title
title_label = ttk.Label(
    master = window,
    text= 'Degrees to Radians',
    font='palatino 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)

entry_Int = tk.IntVar()

entry = ttk.Entry(master=input_frame, textvariable= entry_Int)

button = ttk.Button(master= input_frame, text='Convert', command = convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = "Output",
    font = 'palatino 24',
    textvariable = output_string)
output_label.pack(pady=5)


#run
window.mainloop()
#import modules
import tkinter as tk
from tkinter import ttk

def input_string(entry): #changes values in the output window
    entry_text.set(value= entry_text.get() + str(entry))

def calculate(): #evaluates the string
    string = str(entry_text.get())
    answer = eval(string)
    entry_text.set(value= answer)

def delete(): #deletes the last element of the string
    string = entry_text.get()
    string_deleted = string[:-1]
    entry_text.set(value= string_deleted)
 
#Window
window = tk.Tk()
window.geometry('600x400+0+0')
window.title('Calculator')
window.iconbitmap('Python GUI\Calculator\calculator.ico')

#style
style = ttk.Style()

#input and output window
entry_text = tk.StringVar(value= '')
entry = ttk.Entry(window, textvariable= entry_text, font= 'Ariel 30', justify= 'right')
entry.pack(pady= 10)

# button frame
main_frame = ttk.Frame(window)

frame1 = ttk.Frame(main_frame)
frame2 = ttk.Frame(main_frame)
frame3 = ttk.Frame(main_frame)
frame4 = ttk.Frame(main_frame)


#buttons
btn_1 = ttk.Button(frame1, text='1', style= 'small.TButton', width= '5', command= lambda: input_string(1))
btn_2 = ttk.Button(frame2, text='2', style= 'small.TButton', width= '5', command= lambda: input_string(2))
btn_3 = ttk.Button(frame3, text='3', style= 'small.TButton', width= '5', command= lambda: input_string(3))
btn_4 = ttk.Button(frame1, text='4', style= 'small.TButton', width= '5', command= lambda: input_string(4))
btn_5 = ttk.Button(frame2, text='5', style= 'small.TButton', width= '5', command= lambda: input_string(5))
btn_6 = ttk.Button(frame3, text='6', style= 'small.TButton', width= '5', command= lambda: input_string(6))
btn_7 = ttk.Button(frame1, text='7', style= 'small.TButton', width= '5', command= lambda: input_string(7))
btn_8 = ttk.Button(frame2, text='8', style= 'small.TButton', width= '5', command= lambda: input_string(8))
btn_9 = ttk.Button(frame3, text='9', style= 'small.TButton', width= '5', command= lambda: input_string(9))
btn_0 = ttk.Button(frame2, text='0', style= 'small.TButton', width= '5', command= lambda: input_string(0))
btn_mul = ttk.Button(frame4, text='*', style= 'small.TButton', width= '5', command= lambda: input_string('*'))
btn_div = ttk.Button(frame4, text='/', style= 'small.TButton', width= '5', command= lambda: input_string('/'))
btn_add = ttk.Button(frame4, text='+', style= 'small.TButton', width= '5', command= lambda: input_string('+'))
btn_sub = ttk.Button(frame4, text='-', style= 'small.TButton', width= '5', command= lambda: input_string('-'))
btn_equal = ttk.Button(frame4, text='=', style= 'small.TButton', width= '5', command= calculate)
btn_dot = ttk.Button(frame1, text='.', style= 'small.TButton', width= '5', command= lambda: input_string('.'))
btn_clear = ttk.Button(frame3, text='C', style= 'small.TButton', width= '5', command= lambda: entry_text.set(value= ''))
btn_delte = ttk.Button(frame3, text='←' , style= 'small.TButton', width= '5', command= delete)

#layout
btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
btn_5.pack()
btn_6.pack()
btn_7.pack()
btn_8.pack()
btn_9.pack()
btn_0.pack()
btn_mul.pack()
btn_div.pack()
btn_add.pack()
btn_sub.pack()
btn_equal.pack()
btn_dot.pack()
btn_delte.pack()
btn_clear.pack()

#layout for frames
frame1.pack(side= 'left', fill= 'both', expand= True)
frame2.pack(side= 'left', fill= 'both', expand= True)
frame3.pack(side= 'left', fill= 'both', expand= True)
frame4.pack(side= 'left', fill= 'both', expand= True)

main_frame.pack(pady= 10)

#button styles
style.configure('small.TButton', font=('Ariel', 25))

#run
window.mainloop()
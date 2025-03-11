import tkinter as tk
import ttkbootstrap as ttk
import cv2
from PIL import Image, ImageTk

x = 0

def update_frame():
    global cap, label, x
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        x += 1
        frame_number.set(value= x)
    label.after(10, update_frame)

def play_ip_video(ip_url):
    global cap, label
    cap = cv2.VideoCapture(ip_url)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    
    update_frame()

def on_closing():
    cap.release()
    window.destroy()

#Window
window = ttk.Window()
window.geometry('700x600')
window.title('IP camera')

btn = ttk.Button(window, text= 'EXIT', command= lambda: exit())
btn.pack(pady= 10)

label = ttk.Label(window)
label.pack()

frame_number = tk.IntVar(value= 0)
label2 = ttk.Label(window, textvariable= frame_number, font= 'Calibri 20')
label2.pack()

ip_camera_url = "http://100.117.73.163:8080/video"
play_ip_video(ip_camera_url)

#run
window.mainloop()
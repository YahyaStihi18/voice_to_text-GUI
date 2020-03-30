import speech_recognition as sr
import tkinter as tk
import time, threading
import pyperclip
from PIL import Image, ImageTk
import winsound

r = sr.Recognizer()
# This function takes audio input and return it as a text and save it in file.txt
def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="ar-EG")
        except:
            pass
        file = open('support/file.txt', "a+", encoding="utf-8")
        file.write(voice_data)
        file.write(' ')
        file.close()

        entry['text'] = show_file()
        threading.Timer(10, show_file).start()
        return voice_data

# clear text inside ykinter window
def clear():
    file = open('support/file.txt', "w")
    file.write('')
    file.close()
    entry.delete(1.0, tk.END)

#show data inside the file.txt 
def show_file():

    entry.delete(1.0, tk.END)
    file_r = open("support/file.txt", "r", encoding="utf-8")
    contents = file_r.read()
    entry.insert(tk.END, contents)
    file_r.close()

# show data inside support.txt in tkinter window
def support():
    entry.delete(1.0, tk.END)
    file_s = open("support/support.txt", "r", encoding='utf-8')
    contents = file_s.read()
    entry.insert(tk.END, contents)
    file_s.close()
    winsound.PlaySound("windows.wav", winsound.SND_ASYNC)

# satrt the GUI
root = tk.Tk()
root.title('voice to text')

canvas = tk.Canvas(root, height=500, width=900)
canvas.pack()
background_image = tk.PhotoImage(file='image/bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#3498DB', bd=5)
frame.place(relx= 0.41, rely=0.08, relwidth=0.76, relheight=0.86, anchor='n')

#=============================================================================

entry = tk.Text(frame,font=("jameel noori nastaleeq",14))
entry.place(relx=0, rely=0, relwidth=1, relheight=1)
show_file()
# copy data inside file.txt to clipboard
def copy():
    file_c = open("support/file.txt", "r", encoding="utf-8")
    contents = file_c.read()
    pyperclip.copy(contents)
    file_c.close()


#============== frame's==========================================================
frame1 = tk.Frame(root, bg='#3498DB', bd=3)
frame1.place(relx= 0.81, rely=0.08, relwidth=0.17, relheight=0.09)
micro_i = ImageTk.PhotoImage(Image.open('image/micro.png'))
pane1 = tk.Label(frame1, image=micro_i).place(x=1, y=1)

frame2 = tk.Frame(root, bg='#3498DB', bd=3)
frame2.place(relx= 0.81, rely=0.20, relwidth=0.17, relheight=0.09)
clear_i = ImageTk.PhotoImage(Image.open('image/clear.png'))
panel2 = tk.Label(frame2, image=clear_i).place(x=1, y=1)

frame3 = tk.Frame(root, bg='#3498DB', bd=3)
frame3.place(relx= 0.81, rely=0.32, relwidth=0.17, relheight=0.09)
copy_i = ImageTk.PhotoImage(Image.open('image/copy.png'))
panel3 = tk.Label(frame3, image=copy_i).place(x=1, y=1)

frame4 = tk.Frame(root, bg='#3498DB', bd=3)
frame4.place(relx= 0.81, rely=0.85, relwidth=0.17, relheight=0.09)
support_i = ImageTk.PhotoImage(Image.open('image/support.png'))
panel4 = tk.Label(frame4, image=support_i).place(x=1, y=1)


#============= buttons =======================================================================

button1 = tk.Button(frame1, bg='#CACFD2', text='تسجيل', font=('bold', 14), command=record_audio)
button1.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

button2 = tk.Button(frame2, bg='#CACFD2', text='مسح', font=('bold',14), command=clear)
button2.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

button3 = tk.Button(frame3, bg='#CACFD2', text='نسخ', font=('bold',14), command=copy)
button3.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

button4 = tk.Button(frame4, bg='#CACFD2', text='التعليمات', font=('bold',14), command=support)
button4.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
# run the GUI
root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import ctypes
import AI_main
# Create object

class MainPage:
    def __init__(self):

        root = tk.Tk()
        FONT_TUPLE = ("Comic Sans MS", 14, "bold")
        FILENAME = 'C:\img.png'

        tk_img = ImageTk.PhotoImage(file=FILENAME)
        framer = Label(root, image=tk_img)
        framer.pack(side=TOP, fill=X)
        speak_button = tk.Button(root, text='Speak', command=self.speaker, anchor='e', width=5, bg='light grey',
                                 fg='red4', relief='flat',font=FONT_TUPLE)  # makes a speak button
        speak_button.place(x=650, y=325)
        l1 = tk.Label(root,
                          text='Functionalities Performed: ',fg='red4',bg='light grey', font = "Verdana 10 bold" ).place(x=585,y=400)
        l2=tk.Label(root,text='Open Youtube \n Play Music \n Search Wikipedia \n Tell a joke \n Open Whatsapp ',fg='red4',bg='light grey', font = "Verdana 10 bold",width=20 ).place(x=485,y=450)
        # Width x Height

        l3 = tk.Label(root,
                      text='Open Google \n Show Time \n Open StackOverflow \n Open Code \n Send an Email ',
                      fg='red4', bg='light grey', font="Verdana 10 bold",width=20).place(x=700, y=450)
        # Width x Height
        root.mainloop()


    def speaker(self):
        AI_main.mainClass()

first = MainPage()


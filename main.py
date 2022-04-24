# -*- coding: utf-8 -*-
"""
Created on Sat April 24 13:30:59 2022

@author: Naman Chhabra

Creating a app for translating English to Hindi and vice versa

"""

#   pip install "googletrans==4.0.0rc1"
# Import Libraries

from tkinter import *
from googletrans import Translator, LANGUAGES


# Intialzing Window OR Creating a display Window

Screen = Tk()
Screen.title('Language Translator')
Screen.geometry("1750x750")
Screen.resizable(0,0)


# #
# Creating a function for translating the text
Input = StringVar()
Output = StringVar()


# # Heading
Label(Screen, text="LANGUAGE TRANSLATOR from Hindi to English and vise versa").pack()

# # INPUT TEXT WIDGET
Label(Screen, text="     INPUT : - ").place(x=10, y=60)
Input_text = Text(Screen, wrap=WORD, width=50, height=20)
Input_text.place(x=30, y=100)


# # OUTPUT TEXT WIDGET
Label(Screen, text="     OUTPUT : -  ").place(x=1080, y=60)
Output_text = Text(Screen, wrap=WORD, width=50, height=20)
Output_text.place(x=900, y=100)

# Intial Language And Choice
language = {'english', 'hindi'}
Input.set('english')
Output.set('hindi')

# Chose the input languages
InputMenu = OptionMenu(Screen, Input, *language)
InputMenu.place(x=470, y=50)
Label(Screen, text="Choose a Language :-").place(x=180, y=60)
# print(Input.get())

#  OUTput language
OutputMenu = OptionMenu(Screen, Output, *language)
OutputMenu.place(x=1570, y=50)
Label(Screen, text="Translated Language :-").place(x=1280, y=60)



def Translate():
    lang_translator = Translator()
    text_to_translate = lang_translator.translate(text= Input_text.get(1.0,END), src=Input.get(), dest=Output.get())
    print(text_to_translate.text)
    Output_text.delete(1.0, END)
    Output_text.insert(END, text_to_translate.text)
    

#########  Translate Button ########
trans_btn = Button(Screen, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue', activebackground = 'sky blue')
trans_btn.place(x = 772, y = 50)

# mainloop(): It helps to run the tkinter event loop.
Screen.mainloop()
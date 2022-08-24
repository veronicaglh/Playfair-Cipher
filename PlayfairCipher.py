# This program will be able to receive a plain text and encrypt it using the playfair cipher
# This program will also be able to decrypt a cipher text back into the original message
# In addition it will also have a UI that is built with tkinter.
# For this program to work some packages will need to be installed.
# To install these packages run the following commands on your IDE's terminal
# pip install pillow


from tkinter import *
from PIL import Image, ImageTk


# PART I - TKINTER GUI
myWindow = Tk()
myWindow.title("CyberSecurity")
myWindow.geometry('807x455')
myWindow['background'] = '#1A002D'

load = Image.open('Images\\BackgroundImage.png')
render = ImageTk.PhotoImage(load)
img = Label(myWindow, image=render)
img.place(x=0, y=0)

title1 = Label(myWindow, text="Playfair Cipher", bg="#1A002D", fg='white', font="Calibri 25 bold italic")
title2 = Label(myWindow, text="Encrypt or Decrypt", bg="#1A002D", fg='white', font="Calibri 8 italic")
title3 = Label(myWindow, text="Key: ", bg="#1A002D", fg='white', font="Calibri 10 italic")
title4 = Label(myWindow, text="Message: ", bg="#1A002D", fg='white', font="Calibri 10 italic")

# Making the input entry field for user to input key and plain/cipher text of their choice
userKey = Entry(myWindow, width=25, font="Calibri 10 italic", fg='#484D50', border=2)
userText = Entry(myWindow, width=25, font="Calibri 10 italic", fg='#484D50', border=2)
myWindow.mainloop()
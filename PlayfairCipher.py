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
title3 = Label(myWindow, text="Key: ", bg="#1A002D", fg='white', font="Calibri 11 italic")
title4 = Label(myWindow, text="Message: ", bg="#1A002D", fg='white', font="Calibri 11 italic")

# Making the input entry field for user to input key and plain/cipher text of their choice
userKey = Entry(myWindow, width=25, font="Calibri 10 italic", fg='#484D50', border=2)
userText = Entry(myWindow, width=25, font="Calibri 10 italic", fg='#484D50', border=2)

# Placing the widgets on the window screen
title1.place(x=510, y=108)
title2.place(x=560, y=146)
title3.place(x=470,y=210)
title4.place(x=440,y=240)
userKey.place(x=510, y=210)
userText.place(x=510, y=240)


# Part II - COMPUTATION

# function to encrypt text
def encrypt():
    # userKey.get() will return the value the user enters as a key
    # userKey is the name of the entry field that has been defined above in PART I
    key = userKey.get()
    key = key.replace(" ", "")
    key = key.upper()

    ##########################
    def matrix(x, y, initial):
        return [[initial for i in range(x)] for j in range(y)]

    result = list()
    for c in key:  # storing key
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)

    flag = 0
    for i in range(65, 91):  # storing other character
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    my_matrix = matrix(5, 5, 0)  # initialize matrix
    for i in range(0, 5):  # making matrix
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

    def locindex(c):  # get location of each character
        loc = list()
        if c == 'J':
            c = 'I'
        for i, j in enumerate(my_matrix):
            for k, l in enumerate(j):
                if c == l:
                    loc.append(i)
                    loc.append(k)
                    return loc
    ###################

    # userText.get() will return the value the user enters as a plain
    # It will get the value from the input field named userText which has been defined in PART I as a tkinter entry widget
    msg=userText.get()
    msg=msg.upper()
    msg=msg.replace(" ", "")
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg =msg[:]+'X'
    print("CIPHER TEXT: ",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]), end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]), end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]), end=' ')
        i=i+2


# function to decrypt cipher text
def decrypt():
    # userKey.get() will return the value the user enters as a key
    # It will get the value from the input field named userKey which had been defined above as a tkinter entry widget
    key = userKey.get()
    key = key.replace(" ", "")
    key = key.upper()

    ########################
    def matrix(x, y, initial):
        return [[initial for i in range(x)] for j in range(y)]

    result = list()
    for c in key:  # storing key
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)

    flag = 0
    for i in range(65, 91):  # storing other character
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    my_matrix = matrix(5, 5, 0)  # initialize matrix
    for i in range(0, 5):  # making matrix
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

    def locindex(c):  # get location of each character
        loc = list()
        if c == 'J':
            c = 'I'
        for i, j in enumerate(my_matrix):
            for k, l in enumerate(j):
                if c == l:
                    loc.append(i)
                    loc.append(k)
                    return loc
    ###################

    # userText.get() will return the value the user enters as a plain text
    # It will get the value from the input field named userText which had been defined above, as a tkinter entry widget
    msg = userText.get()
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("PLAIN TEXT: ",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')
        i=i+2


EncryptButton = Button(myWindow, text="Encrypt", bg="#f4c5dc", font="Calibri 8 italic", command=encrypt)
EncryptButton.place(x=600, y=270)
DecryptButton = Button(myWindow, text="Decrypt", bg="#f4c5dc", font="Calibri 8 italic", command=decrypt)
DecryptButton.place(x=650, y=270)
myWindow.mainloop()
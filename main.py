from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror, showinfo
import os

win = Tk()
win.title('NEAN EDITOR')
win.configure(background="black")
win.geometry('1234x700')

file_path = ''

lbl1 = Label(win, text='N\nE\nA\nN\n\nE\nD\nI\nT\nO\nR',fg="cyan",bg="black" , font=('arial',20,'bold')).place(x = 15, y = 5)

def set_file_path(path):

    global file_path
    file_path = path

def open_file():

    path = askopenfilename(filetypes=[('HTML Files', '*.html')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():

    if file_path == '':
        path = asksaveasfilename(filetypes=[('HTML Files', '*.html')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)
  
def about():

    showinfo('NEAN EDITOR',"HTML Editor \nCreated by: Ahmed Nazran\nCreated in: 16/3/2022")

def run():

    path = file_path
    if file_path == '':
        showerror('NEAN EDITOR',"Please save the file")
    else:
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)
        os.startfile(file_path)

menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Output', command=run)
menu_bar.add_cascade(label='about',command=about)
win.config(menu=menu_bar)

editor = Text(fg="cyan", width=102, height=29, insertbackground="white", bg="#292828",font=('arial',15))
editor.pack()
start_txt = """<!DOCTYPE html>
<html lang="en">
<head>
              <meta charset="UTF-8">
              <meta http-equiv="X-UA-Compatible" content="IE=edge">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>Document</title>
</head>
<body>
              <p>Hello World</p>
</body>
</html>
"""
editor.insert('1.0',start_txt)

win.mainloop()

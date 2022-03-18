from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror, showinfo
import os

win = Tk()
win.title('NEAN EDITOR')
win.configure(background="black")
win.geometry('1234x700')

file_path = ''

name = Label(win, text='N\nE\nA\nN\n\nE\nD\nI\nT\nO\nR',fg="cyan",bg="black" , font=('arial',20,'bold')).place(x = 15, y = 5)

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

    showinfo('NEAN EDITOR',"Web Editor \nCreated by: Ahmed Nazran\nCreated in: 16/3/2022")

file_pathcss = ''
def set_file_path_css(csspath):

    global file_pathcss
    file_pathcss = csspath

def open_file_css():

    csspath = askopenfilename(filetypes=[('CSS Files', '*.css')])
    with open(csspath, 'r') as file:
        ccode = file.read()
        css.delete('1.0', END)
        css.insert('1.0', ccode)
        set_file_path_css(csspath)

def save_as_css():

    if file_pathcss == '':
        csspath = asksaveasfilename(filetypes=[('CSS Files', '*.css')])
    else:
        csspath = file_pathcss
    with open(csspath, 'w') as file:
        ccode = css.get('1.0', END)
        file.write(ccode)
        set_file_path_css(csspath)

def run():
    
    pathcss = file_pathcss
    if file_pathcss == '':
        showerror('NEAN EDITOR',"Please save the css file")
    else:
        with open(pathcss, 'w') as cfile:
            ccode = css.get('1.0', END)
            cfile.write(ccode)
            set_file_path_css(pathcss)

    path = file_path
    if file_path == '':
        showerror('NEAN EDITOR',"Please save the html file")
    else:
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)
        os.startfile(file_path)

menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label='Open (html)', command=open_file)
file_menu.add_command(label='Open (css)', command=open_file_css)
file_menu.add_command(label='Save (html)', command=save_as)
file_menu.add_command(label='Save (css)', command=save_as_css)
file_menu.add_command(label='Save As (html)', command=save_as)
file_menu.add_command(label='Save As (css)', command=save_as_css)
file_menu.add_command(label='Exit', command=exit)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Output', command=run)
menu_bar.add_cascade(label='about',command=about)
win.config(menu=menu_bar)

editor = Text(fg="cyan", width=102, height=15, insertbackground="white", bg="#292828",font=('arial',15))
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

css = Text(fg="white", width=102, height=15, insertbackground="white", bg="#292828",font=('arial',15))
css.pack()
csstxt = """/*Enter your css here*/
"""
css.insert('1.0',csstxt)

win.mainloop()
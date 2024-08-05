from tkinter import *
import tkinter as tk
import subprocess
import cmd

Window = tk.Tk() 
Window.title("Green Studio")
Window.geometry("{}x{}+0+0".format(Window.winfo_screenwidth(), Window.winfo_screenheight()))

inputtxt = tk.Text(Window,
                   height = 50,
                   width = 200) 

Command = inputtxt.get(1.0, "end-1c")

terminal = tk.Text(Window,
                   height = 10,
                   width = 200)
def error():
    ErrorPrompt = tk.Tk()
    ErrorPrompt.title("Error")
    ErrorPrompt.geometry("250x250")
    label = tk.Label(ErrorPrompt, text = "There was an error from the user, you")
    label.pack()

def Hi():
    print("Hi")

Filedir = ""
compath = ""

def Newprompt():
    NewPrompt = tk.Tk()
    NewPrompt.title("New prompt")
    NewPrompt.geometry("250x250")
    Filetxt = tk.Text(NewPrompt,
                    bg= 'lightblue',
                   height = 1,
                   width = 25)
    Filetxt.pack()
    def new():
        global Filedir
        Filedir = Filetxt.get(1.0, "end-1c")
        f = open(Filedir, "x")
        NewPrompt.destroy()
    B = Button(NewPrompt, text ="New File", command = new)
    B.pack()


def Openprompt():
    OpenPrompt = tk.Tk()
    OpenPrompt.title("Open prompt")
    OpenPrompt.geometry("250x250")
    Filetxt = tk.Text(OpenPrompt,
                    bg= 'lightblue',
                   height = 1,
                   width = 25)
    Filetxt.pack()
    def openf():
        global Filedir
        Filedir = Filetxt.get(1.0, "end-1c")
        f = open(Filedir, "r")
        print(f.read())
        OpenPrompt.destroy()
    B = Button(OpenPrompt, text ="Open File", command = openf)
    B.pack()

def Saveprompt():
    SavePrompt = tk.Tk()
    SavePrompt.title("Save prompt")
    SavePrompt.geometry("250x250")
    Filetxt = tk.Text(SavePrompt,
                    bg= 'lightblue',
                   height = 1,
                   width = 25)
    Filetxt.pack()
    def save():
        global Filedir
        Filedir = Filetxt.get(1.0, "end-1c")
        f = open(Filedir, "w")
        Command = inputtxt.get(1.0, "end-1c")
        f.write(Command)
        f.close()
        SavePrompt.destroy()
    B = Button(SavePrompt, text ="Save File", command = save)
    B.pack()

def Savefile():
    if Filedir == "":
        Window.destroy()
    else:
        f = open(Filedir, "w")
        Command = inputtxt.get(1.0, "end-1c")
        f.write(Command)
        f.close()

def setupcompiler():
    SetupPrompt = tk.Tk()
    SetupPrompt.title("Setup prompt")
    SetupPrompt.geometry("250x250")
    Filetxt = tk.Text(SetupPrompt,
                    bg= 'lightblue',
                   height = 1,
                   width = 25)
    Filetxt.pack()
    def Set():
        global compath
        compath = Filetxt.get(1.0, "end-1c")
        SetupPrompt.destroy()
    B = Button(SetupPrompt, text ="Done", command = Set)
    B.pack()

def Runcompiler():
    global compath
    if compath == "":
        error()
    else:
        command = compath
        output = subprocess.check_output(command, shell=True, text=True)
        terminal.insert(END, output)
        subprocess.check_output()

menubar = Menu(Window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=Newprompt)
filemenu.add_command(label="Open", command=Openprompt)
filemenu.add_command(label="Save", command=Savefile)
filemenu.add_command(label="Save as", command=Saveprompt)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Window.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy", command=Hi)
editmenu.add_command(label="Paste", command=Hi)
editmenu.add_separator()
editmenu.add_command(label="Undo", command=Hi)
editmenu.add_command(label="Redo", command=Hi)
menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Light mode", command=Hi)
viewmenu.add_command(label="Dark mode", command=Hi)
menubar.add_cascade(label="View", menu=viewmenu)

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Run", command=Runcompiler)
runmenu.add_command(label="Setup", command=setupcompiler)
menubar.add_cascade(label="Run", menu=runmenu)

hmenu = Menu(menubar, tearoff=0)
hmenu.add_command(label="How to", command=Hi)
hmenu.add_command(label="About", command=Hi)
hmenu.add_separator()
hmenu.add_command(label="Exit", command=Window.destroy)
menubar.add_cascade(label="Help", menu=hmenu)

Window.config(menu=menubar)
inputtxt.pack()
terminal.pack()
Window.mainloop()

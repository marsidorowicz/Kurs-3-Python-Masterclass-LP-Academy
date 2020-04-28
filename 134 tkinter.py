import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("HelloWorld")
mainWindow.geometry("640x480+150+150")

label = tkinter.Label(mainWindow, text="Hello")
label.pack(side="top")

leftFrane = tkinter.Frame(mainWindow)
leftFrane.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

rightFrane = tkinter.Frame(mainWindow)
rightFrane.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrane, text="Przycisk 1")
button2 = tkinter.Button(rightFrane, text="Przycisk 2")
button3 = tkinter.Button(rightFrane, text="Przycisk 3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
mainWindow.mainloop()
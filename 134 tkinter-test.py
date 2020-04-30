import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("HelloWorld")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Hello")
label.grid(row=0, column=0)

leftFrane = tkinter.Frame(mainWindow)
leftFrane.grid(row=1, column=1)

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

rightFrane = tkinter.Frame(mainWindow)
rightFrane.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrane, text="Przycisk 1")
button2 = tkinter.Button(rightFrane, text="Przycisk 2")
button3 = tkinter.Button(rightFrane, text="Przycisk 3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrane.config(relief="sunken", borderwidth=1)
rightFrane.config(relief="sunken", borderwidth=1)
leftFrane.grid(sticky="ns")
rightFrane.grid(sticky="new")

rightFrane.columnconfigure(0, weight=1)
button2.grid(sticky="ew")
mainWindow.mainloop()
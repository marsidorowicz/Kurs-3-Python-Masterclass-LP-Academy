import tkinter
import os

char_list = [
    [("C", 1), ("CE", 1)],
    [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
    [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
    [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
    [("0", 1), ("=", 1), ("/", 1)]
]

mainWindow = tkinter.Tk()
mainWindow.title("Kalkulator Mario")
mainWindow.geometry("540x480+1000+200")
mainWindow.minsize(540, 480)
mainWindowPadding = 10
mainWindow["padx"] = mainWindowPadding

# Wyświetlacz
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky="nsew")

# Keypad
key_pad = tkinter.Frame(mainWindow)
key_pad.grid(row=1, column=0, sticky="nsew")
row = 0
for item in char_list:
    col = 0
    for i in item:
        tkinter.Button(key_pad, text=i[0]).grid(row=row, column=col, columnspan=i[1], sticky=tkinter.E + tkinter.W)
        col += i[1]
    row += 1

mainWindow.update()
mainWindow.minsize(key_pad.winfo_width() + mainWindowPadding, result.winfo_height() + key_pad.winfo_height())
mainWindow.maxsize(key_pad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + key_pad.winfo_height())
mainWindow.mainloop()
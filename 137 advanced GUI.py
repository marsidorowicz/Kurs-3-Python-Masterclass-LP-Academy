import tkinter
import os

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Mario Landia")
mainWindow.geometry("640x480+200+200")
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Mój pierwszy GUI")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief="sunken")
for zone in os.listdir("c:/windows/system32"):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1,column=1, sticky="nsw", rowspan=2)
fileList['yscrollcommand'] = listScroll.set

#frame od guzików radio
optionFrame = tkinter.LabelFrame(mainWindow, text="Szczegóły pliku")
optionFrame.grid(row=1, column=2, sticky="ne")

rbValue = tkinter.IntVar()
rbValue.set(1)

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Nazwa pliku", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Ścieżka pliku", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Znak czasu", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=1, column=0, sticky="w")
radio3.grid(row=2, column=0, sticky="w")

# widget wyświetlający wynik
resultLabel = tkinter.Label(mainWindow, text="Szczegóły")
resultLabel.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky="sw")

#Frame na time
timeFrame = tkinter.LabelFrame(mainWindow, text="Czas")
timeFrame.grid(row=3, column=0, sticky="new")

# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondsSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondsSpinner.grid(row=0, column=4)
timeFrame['padx'] = 30

# Frame to spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# Date labels
dayLabel = tkinter.Label(dateFrame, text="Dzień")
monthLabel = tkinter.Label(dateFrame, text="Miesiąc")
yearLabel = tkinter.Label(dateFrame, text="Rok")
dayLabel.grid(row=0, column=0, sticky="w")
monthLabel.grid(row=0, column=1, sticky="w")
yearLabel.grid(row=0, column=2, sticky="w")
# Date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Sty", "Lut", "Mar", "Kwi", "Maj", "Cze", "Lip", "Sie", "Wrz",
                                                        "Paź", "Lis", "Gru"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Przyciski
okB = tkinter.Button(mainWindow, text="OK")
cB = tkinter.Button(mainWindow, text="Wyjdź", command=mainWindow.destroy)
okB.grid(row=4, column=3, sticky="e")
cB.grid(row=4, column=4, sticky="w")
mainWindow.mainloop()

print(rbValue.get())
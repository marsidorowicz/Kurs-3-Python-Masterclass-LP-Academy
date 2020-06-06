import sqlite3
import tkinter

conn = sqlite3.connect('music.sqlite')

mainWindow = tkinter.Tk()

# screen setup
mainWindow.title("Music Browser")
mainWindow.geometry("800x600")
mainWindow.configure(background="black")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1) # distance

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ++ labels ++
tkinter.Label(mainWindow, text="Artysta").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Album").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Piosenki").grid(row=0, column=2)

# ++ Artists list ++
artistsList = tkinter.Listbox(mainWindow)
artistsList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
artistsList.config(border=2, relief='sunken')

artistsScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistsList.yview)
artistsScroll.grid(row=1,column=0, sticky='nsw', rowspan=2)
artistsList['yscrollcommand'] = artistsScroll.set

# ++ Albums list ++
albumsListV = tkinter.Variable(mainWindow)
albumsListV.set(("Wybierz Artystę",))
albumsList = tkinter.Listbox(mainWindow, listvariable=albumsListV)
albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumsList.config(border=2, relief='sunken')

albumsScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistsList.yview)
albumsScroll.grid(row=1,column=1, sticky='nsw', rowspan=2)
albumsList['yscrollcommand'] = albumsScroll.set

# ++ Song list ++
songsListV = tkinter.Variable(mainWindow)
songsListV.set(("Wybierz album",))
songsList = tkinter.Listbox(mainWindow, listvariable=songsListV)
songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
artistsList.config(border=2, relief='sunken')



#
# for artist, album, song, track in conn.execute("SELECT name, 'name:1', title, track FROM artist_list"):
#     artistsList.insert(tkinter.END, artist)

test_list = range(100)
albumsListV.set(tuple(test_list))
mainWindow.mainloop()
conn.close()

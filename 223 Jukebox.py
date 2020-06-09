import sqlite3
import tkinter


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs, exportselection=False)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # store id of record we populate from
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)  # TODO: delete
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO delete this later
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear listbox
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)  # TODO delete
            index = self.curselection()[0]
            value = self.get(index),

            # get id from database row
            # check if value is is correct, by including link_value if appropriate
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"

            # retrieve artist name from database row
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            self.linked_box.requery(link_id)
            # artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
            # alist = []
            # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name",
            # artist_id):
            #     alist.append(row[0])
            # albumsListV.set(tuple(alist))
            # songsListV.set(("Wybierz Album",))


# def get_songs(event):
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     album_name = lb.get(index),
#
#     # retrieve artist id  from database rowspan
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
#     alist = []
#     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.title", album_id):
#         alist.append(x[0])
#     songsListV.set(tuple(alist))
if __name__ == "__main__":
    conn = sqlite3.connect('music.sqlite')

    mainWindow = tkinter.Tk()

    # screen setup
    mainWindow.title("Music Browser")
    mainWindow.geometry("800x600")
    mainWindow.configure(background="green")

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)   # distance

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ++ labels ++
    tkinter.Label(mainWindow, text="Artysta").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Album").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Piosenki").grid(row=0, column=2)

    # ++ Artists list ++
    artistsList = DataListBox(mainWindow, conn, "artists", "name", background="black", fg="white")
    artistsList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistsList.config(border=2, relief='sunken')

    artistsList.requery()

    # ++ Albums list ++
    albumsListV = tkinter.Variable(mainWindow)
    albumsListV.set(("Wybierz Artystę",))
    albumsList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",), listvariable=albumsListV, background="black", fg="white")
    # albumsList.requery()
    albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    albumsList.config(border=2, relief='sunken')

    # albumsList.bind("<<ListboxSelect>>", get_songs)
    artistsList.link(albumsList, "artist")

    # ++ Song list ++
    songsListV = tkinter.Variable(mainWindow)
    songsListV.set(("Wybierz Album",))
    songsList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title",), listvariable=songsListV, background="black", fg="white")
    # songsList.requery()
    songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
    songsList.config(border=2, relief='sunken')

    albumsList.link(songsList, "album")

    mainWindow.mainloop()
    conn.close()

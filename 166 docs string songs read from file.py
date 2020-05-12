class Song:
    """Class representing a song
    """

    def __init__(self, title, artist, duration=0):
        # """Song init method
        #
        # :param title: str: Initialised song title
        # :param artist: str: Initialised song artist
        # :param duration: int: Initialised song duration, default 0
        # """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title
    name = property(get_title)


# help(Song.__init__)
# help(Song)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
Song.__init__.__doc__ = """Song init method

        :param title: str: Initialised song title
        :param artist: str: Initialised song artist
        :param duration: int: Initialised song duration, default 0
        """


class Album:
    """Class representing an album, using its track_list
    Atributes:
        name: str: The name of the album.

    Methods:
          addSong: Used to add a song to the album track_list.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
        else:
            self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist information

    Atributes:
        name (str): The name of the artist.
        albums (list(Album)): A list of the albums by this artist.

    Methods:
        add_album: Use to add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Adds a new album to the artist's album list

        Args:
            album (Album): Album object to add to the list.
            If the album already exists, it will not add it again.
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Adds a song to the album"""
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Is object in already"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # Linia w pliku powinna zawierać (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from object data for comp, with original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(len(artists))
    create_checkfile(artists)
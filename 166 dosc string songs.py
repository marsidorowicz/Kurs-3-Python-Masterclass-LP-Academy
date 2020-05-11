class Song:

    def __init__(self, title, artist, duration=0):
        """

        :param title: str: Initialised song title
        :param artist: str: Initialised song artist
        :param duration: int: Initialised song duration, default 0
        """
        self.title = title
        self.artist = artist
        self.duration = duration

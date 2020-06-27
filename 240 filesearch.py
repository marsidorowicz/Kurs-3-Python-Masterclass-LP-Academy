import os
import fnmatch


def find_file_name(root, filename=None, start=None, ext=None):
    if filename:
        if start:
            for path, directories, files in os.walk(root):
                if start in path:
                    for file in (f for f in files if fnmatch.fnmatch(f, filename)):
                        if ext:
                            file_name, file_ext = os.path.splitext(file)
                            if ext in file_ext:
                                yield os.path.abspath(path) + "\\" + file
                        else:
                            yield os.path.abspath(path) + "\\" + file
        else:
            for path, directories, files in os.walk(root):
                for file in (f for f in files if fnmatch.fnmatch(f, filename)):
                    if ext:
                        file_name, file_ext = os.path.splitext(file)
                        if ext == file_ext:
                            yield os.path.abspath(path) + "\\" + file
                    else:
                        yield os.path.abspath(path) + "\\" + file
    else:
        if start:
            for path, directories, files in os.walk(root):
                if start in path:
                    for file in files:
                        file_name, file_ext = os.path.splitext(file)
                        if ext:
                            if ext == file_ext:
                                yield os.path.abspath(path) + "\\" + file
                        else:
                            yield os.path.abspath(path) + "\\" + file
        else:
            for path, directories, files in os.walk(root):
                for file in files:
                    file_name, file_ext = os.path.splitext(file)
                    if ext:
                        if ext == file_ext:
                            yield os.path.abspath(path) + "\\" + file
                    else:
                        yield os.path.abspath(path) + "\\" + file


def find_albums_on_disk(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):  # without case sensitivity in file sys
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):  # linux
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):  # mac and linux
            sub_dir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(sub_dir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


# album_list = find_albums_on_disk("music", "black*")
# song_list = find_songs(album_list)
#
# for s in song_list:
#     print(s)
# # for a in album_list:
# #     print(a)
file_list = find_file_name("music",  ext=".emp3")

for f in file_list:
    print(f)
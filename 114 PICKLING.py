import pickle

# text = ('Mario G',
#         'Mario L',
#         '2020',
#         ((1, "Strzała"),
#          (2, "Jeżyk"),
#          (3, "Flądra")))

# with open("E:\\mario.pickle", "wb") as pickle_file:
#     pickle.dump(text, pickle_file)
# with open("E:\\mario.pickle", "rb") as mario_pickled:
#     text2 = pickle.load(mario_pickled)
#
# print(text2)
# album, artist, year, track_list = text2
# print(album)
# print(artist)
# print(year)
# print(track_list)
#
# for track in track_list:
#     item_number, item_title = track
#     print(item_number, item_title)
#
text = ('Mario G',
        'Mario L',
        '2020',
        ((1, "Strzała"),
         (2, "Jeżyk"),
         (3, "Flądra")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("E:\\mario.pickle", "wb") as pickle_file:
    pickle.dump(text, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
import random
import tkinter

mainWindow = tkinter.Tk()

# Screen setup
mainWindow.title("Gra Black Jack")
mainWindow.geometry("640x480")


def load_images(card_images):
    suits = ["heart", "clubs", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # retrieve image for each suit
    for suit in suits:
        # numbered cards
        for card in range(1, 11):
            name = "E:/programowanie/cards/{}_{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(tile=name)
            card_images.append((card, image,))

        # face cards
        for card in face_cards:
            name = "E:/programowanie/cards/{}_{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(tile=name)
            card_images.append((10, image,))

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, relief="sunken", borderwidth=1, background="green")
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textVariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Frame to hold card images
dealer_card_frame = tkinter.Label(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Gracz", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textVariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Frame to hold card images
player_score_frame = tkinter.Frame(card_frame, background="green")
player_score_label.grid(row=2, column=1, columnspan="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer")
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Gracz")
player_button.grid(row=0, column=1)

# load card_images
cards = []
load_images(cards)

# create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# 2 lists player and dealer cards
dealer_hand = []
player_hand = []


mainWindow.mainloop()
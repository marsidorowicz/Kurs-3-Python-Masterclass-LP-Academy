def python_food():
    width = 80
    text = "Jajecznica"
    left_margin = (width -len(text)) // 2
    print(" " * left_margin, text)


def center_text(text):
    left_margin = (150 - len(text)) // 2
    print(" " * left_margin, text)


def center_text_ex(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (150 - len(text)) // 2
    return " " * left_margin + text

# with open("centered", mode="w") as centered_file:
# call
print(center_text_ex("Jajecznica sobie czeka"))
center_text("Jajko i jajko")
center_text_ex("jeden", "dwa", "trzy", sep=":")

with open("menu", "w") as menu:
    print(center_text_ex("Kurczak"), file=menu)
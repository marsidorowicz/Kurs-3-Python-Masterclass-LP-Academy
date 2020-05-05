def spam1():

    def spam2():

        def spam3():
            z = " dużo więcej spamu"
            print("Zmienne w spam3 to {}".format(locals()))
            return z

        y = " więcej spamu"
        y += spam3()
        print("Zmienne w spam2 to {}".format(locals()))
        return y

    x = "spam"
    x += spam2()
    print("Zmienne w spam1 to {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())
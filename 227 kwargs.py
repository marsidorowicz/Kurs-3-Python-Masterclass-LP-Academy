# def print_backwards(*args, end=" ", **kwargs):
def print_backwards(*args, end=" ", **kwargs):
    for word in args[::-1]:
        print(word[::-1], end=end, **kwargs)


print_backwards("Konstantynopolitańczykiewiczówka", "wwwwe", end='\n')
print_backwards("Konstantynopolitańczykiewiczówka", "wwwwe", end='\n', sep="|")
print_backwards("Another string", end=' ')

def average(*args):
    print(type(args))
    print("args is {}".format(args))
    print("args is: ", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    # tuple_from_args = []
    # for arg in args:
    #     tuple_from_args.append(arg)
    # return tuple(tuple_from_args)
    return args

#
# print(average(1, 2, 3, 4))


message = build_tuple("Raz", "Dwa", "Trzy")
print(type(message))
print(message)

numbers = build_tuple(1, 2, 3)
print(type(numbers))
print(numbers)
#string = "1234567890"
list = [1, 2, 3, 4, 5, 6]

# for char in string:
#     print(char)
my_iterator = iter(list)
print(my_iterator)
for i in range(len(list)):
    print(next(my_iterator))

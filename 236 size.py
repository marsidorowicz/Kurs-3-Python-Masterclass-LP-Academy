import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


big_range = my_range(5)  # dane w zmiennej big_range można użyć raz, żeby skorzystać ponownie należy używać
                        # generatora jeszcze raz, przyczyna funkcja my_range to generator

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# crate list

big_list = []
for val in big_range:
    big_list.append(val)

print("big_range is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
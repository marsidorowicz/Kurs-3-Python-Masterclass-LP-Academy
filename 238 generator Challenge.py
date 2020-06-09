def odd_gen():
    current = 1
    while True:
        yield current
        current = current + 2

#
#
# odd = odd_gen()
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))


def  pi():
    odds = odd_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


aprox_pi = pi()

for x in range(10000000):
    print(next(aprox_pi))
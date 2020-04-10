for i in range(1, 13):
    print("Wynik dla i = {0:2} i do kwadratu = {1:3} a i do potęgi trzeciej = {2:4}".format(i, i**2, i**3))

print()

for i in range(1, 13):
    print("Wynik dla i = {0:2} i do kwadratu = {1:<3} a i do potęgi trzeciej = {2:<4}".format(i, i**2, i**3))

print()

print("Pi wynosi w przybliżeniu {0:12}".format(22/7))
print("Pi wynosi w przybliżeniu {0:12f}".format(22/7))
print("Pi wynosi w przybliżeniu {0:12.50f}".format(22/7))
print("Pi wynosi w przybliżeniu {0:52.50f}".format(22/7))
print("Pi wynosi w przybliżeniu {0:62.50f}".format(22/7))
print("Pi wynosi w przybliżeniu {0:<72.50f}".format(22/7))
print("Pi wynosi w przybliżeniu {0:<72.54f}".format(22/7))

for i in range(1, 13):
    print("Wynik {} i do kwadratu = {} a i do potęgi trzeciej = {:<4}".format(i, i**2, i**3))

print(f"Pi wynosi w przybliżeniu {22 / 7:12.12f}")
pi = 22/7
print(f"Pi wynosi w przybliżeniu {pi:12.20f}")
# farma = {"kot", "owca", "krowa"}
# print(farma)
#
# for zwierze in farma:
#     print(zwierze)
#
# print("*"*80)
#
# dzikie = set(["lew", "lampart", "jeleń"])
# print(dzikie)
#
# for zwierze in dzikie:
#     print(zwierze)
#
# farma.add("koń")
# dzikie.add("koń")
# print(farma)
# print(dzikie)
# pusty_set = set()
# kwadraty_tuple = (4, 6, 9, 16, 25)
# kwadraty = set(kwadraty_tuple)
# print(kwadraty)
# squares = set(squares_tuple)
# print(squares)
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("#" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
#
# print("Różnica sumetryczna")
# print(sorted(even.symmetric_difference(squares)))
#
# print("Różnica symetryczna sq - even")
# print(squares.symmetric_difference(even))

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
squares.remove(8)
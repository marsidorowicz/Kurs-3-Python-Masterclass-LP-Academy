print(__file__)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

number = int(input("Podaj liczbę a pokaże jej kwadrat: "))

squares = []
for number in numbers:
    squares.append((number ** 2))

index_pos = numbers.index(number) # dont use same name in loop and for input
print(squares[index_pos])
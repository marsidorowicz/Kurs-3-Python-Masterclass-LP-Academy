print(__file__)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

number = int(input("Podaj liczbę a pokaże jej kwadrat: "))

squares = [number ** 2 for number in numbers]

index_pos = numbers.index(number) # in list comprehension no side effects here
# automatically protect variables
print(squares[index_pos])
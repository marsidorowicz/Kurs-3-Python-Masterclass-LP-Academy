numbers = [1, 12, 31, 11, 60]

for number in numbers:
    if number % 8 == 0:
        print("Te liczby nie są dozwolone")
        break
else:
    print("Wszystkie liczby są dozwolone")
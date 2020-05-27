def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n - 1)


# try:
#     print(factorial(1000))
# except RecursionError:
#     print("Przekroczono maksymalną liczbę dopuszzalną w funkcji")
# except ZeroDivisionError:
#     print("Dzielisz przez zero!")

try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("Przekroczono maksymalną liczbę dopuszczalną w funkcji")


print("Program terminating...")
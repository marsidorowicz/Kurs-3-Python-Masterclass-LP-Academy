# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit

 
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def test1():
    fact(100)


def test2():
    factorial(100)


result_1 = timeit.timeit(test1, globals=globals(), number=10000)
result_2 = timeit.timeit(test2, globals=globals(), number=10000)
print(result_1)
print(result_2)
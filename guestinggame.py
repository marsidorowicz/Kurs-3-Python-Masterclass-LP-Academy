import random

highest = 10

answer = random.randint(1, 10)
guess = i = 0
while guess != answer or guess == 0:
    print("Zgadnij liczbę między 1 i {}: ".format(highest))
    guess = int(input())

    if guess == answer and i == 0:
        print("Udało Ci się za pierwszym razem")
        break
    if guess == answer and i != 0:
        print("Udało Ci się za {} razem :)".format(i+1))
    else:
        if guess < answer:
            print("Za mało")
            i += 1
        else:
            print("Za dużo")
            i +=1

# if guess != answer:
#     if guess < answer:
#         print("Za mało")
#     else:
#         print("Za dużo")
#     guess == int(input())
#     if guess == answer:
#         print("Brawo, udało Ci się!")
#     else:
#         print("To nie ta liczba")
# else:
#     print("Udało Ci się za pierwszym razem")

# if guess < answer:
#     print("Za mało :) ")
#     guess = int(input())
#     if guess == answer:
#         print("Brawo, zgadłeś ")
#     else:
#         print("Niestety znów nie zgadłeś")
# elif guess > answer:
#     print("Za dużo")
#     guess = int(input())
#     if guess == answer:
#         print("Brawo, zgadłeś ")
#     else:
#         print("Niestety znów nie zgadłeś")
# else:
#     print("Zgadłeś za pierwszym razem !")
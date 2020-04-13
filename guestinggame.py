answer = 5

print("Zgadnij liczbę między 1 i 10: ")
guess = int(input())

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
answer = 5
if guess == answer:
    print("Udało Ci się za pierwszym razem")
else:
    if guess < answer:
        print("Za mało")
    else:
        print("Za dużo")
    guess = int(input())
    print(guess)
    if guess == answer:
        print("Brawo, udało Ci się!")
    else:
        print("To nie ta liczba")
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
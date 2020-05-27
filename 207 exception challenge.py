# def check(arg1, arg2):
#     try:
#         arg1 = int(arg1)
#         arg2 = int(arg2)
#         x = arg1 / arg2
#         print(x)
#     except (TypeError, ZeroDivisionError, ValueError):
#         print("Jakiś błąd")
#
#
# a = input("Podaj pierwszą liczbę: ")
# b = input("Podaj pierwszą liczbę: ")
# check(a, b)
import sys


def calc(arg1, arg2):
    try:
        result = arg1 / arg2
        print(result)
    except (ValueError, ZeroDivisionError, TypeError):
        print("Wystąpił błąd obliczeń, kończę program...")  # pokaże się jak błąd będzie jednym z trzech wybranych
    except EOFError:
        sys.exit(1)
    else:
        print("Zadziałała funkcja dzielenia")  # pokaże się tylko gdy try zadziała


def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Podano niewłaściwą liczbę, spróbuj ponownie: ")
        except EOFError:
            sys.exit(2)
        except:
            print("Błąd")  # ogólne błędy, bez określania który, czyli wszystkie
        finally:  # dobre na zamknięcie bazy danych albo pliku, wykona się zanim program się zakończy
            print("Zawsze się włącza")


a = get_number("Podaj pierwszą liczbę: ")
b = get_number("Podaj drugą liczbę: ")
calc(a, b)

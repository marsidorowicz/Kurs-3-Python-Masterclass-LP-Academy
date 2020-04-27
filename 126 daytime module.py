# import time
#
# print("Epoka " +time.strftime("%c", time.gmtime(0)))
# print("Strefa czasowa to {0}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("Aktywny czas letni")
#     print("To : " + time.tzname[1])
#
# print("Czas lokalny to " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
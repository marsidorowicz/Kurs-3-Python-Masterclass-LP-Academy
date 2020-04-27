import time
#
# print(time.gmtime(0))
# # print(time.localtime(time.time()))
# # print(time.time())
# time_here = time.localtime()
# print(time_here)
# print("Rok", time_here[0], time_here.tm_year)
# print("Miesiąc", time_here[1], time_here.tm_mon)
# print("Dzień", time_here[2], time_here.tm_mday)

from time import perf_counter as my_timer
# from time import monotonic as my_timer
# from time import process_time as my_timer
# from time import time as my_timer
import random

input("Naciśnij enter aby zacząć")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Naciśnij enter aby zatrzymać")
end_time = my_timer()

print("Zaczęto o : " + time.strftime("%X", time.localtime(start_time)))
print("Zakończono o : " + time.strftime("%X", time.localtime(end_time)))

print("Czas twojej reakcji to {} sekund".format(end_time - start_time))
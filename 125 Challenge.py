import time

my_1 = time.time()
my_2 = time.perf_counter()
my_3 = time.monotonic()
my_4 = time.perf_counter()

print(my_1)
print(my_2)
print(my_3)
print(my_4)
print("#"*40)
print("time():\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))

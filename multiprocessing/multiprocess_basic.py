from time import *
from multiprocessing import *

start = perf_counter()

def do_something(seconds_given):
    print("Hello am doing multiprocess")
    sleep(seconds_given)
    print("after sleep")


p = Process(target=do_something)
p1 = Process(target=do_something)
p2 = Process(target=do_something)
p.start()
p1.start()
p2.start()
p.join()
p1.join()
p2.join()

finish = perf_counter()
print(round(finish-start))

start_loop = perf_counter()
processes = []
for _ in range(100):
    p = Process(target=do_something,args = [2])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish_loop = perf_counter()

print(round(finish_loop-start_loop))
'''
multi threading



'''

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)



class Hai(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)



hello = Hello()
hi = Hai()

hello.start()

hi.start()
print(enumerate()) # returns the threads [<_MainThread(MainThread, started 4770412032)>, <Hello(Thread-1, started 123145575288832)>, <Hai(Thread-2, started 123145580544000)>]
print(active_count()) # active threads count

print("This will execute before thread complete because it is not joined to main thread ")

hello.join() #if you use join it will wait for end of the threads and excutes the next lines of code
hi.join()

print("This will print after thread complete")
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("hello")
            sleep(1)



class Hai(Thread):
    def run(self):
        for i in range(50):
            print("hi")
            sleep(1)



hello = Hello()
hi = Hai()

hello.start()
hi.start()

print("before thread join use hello hi")

hello.join()
hi.join()

print("after hello hi")
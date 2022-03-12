# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

from abc import ABC,abstractmethod

class Computer(ABC):
    
    @abstractmethod
    def run(self):
        print("hello")
    
# v = Computer()
# v.run()
        
class Laptop(Computer):
    def run(self):
        print("it runs")
c = Laptop()
c.run()

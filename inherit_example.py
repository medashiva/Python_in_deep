''''

single inheritance

    1) super().__init()__ to pass the parent class values

'''

class MovingMachine:
    def __init__(self,name,tyres,type):
        self.name = name
        self.tyres = tyres
        self.type = type

    def vehicle_type(self):
        return self.type



class Car(MovingMachine):

    def __init__(self,name,tyres,type,make):

        super().__init__(name,tyres,type)
        self.make= make


    def make_of_vehicle(self):
        value = self.vehicle_type()+" "+self.make
        return value




c = Car('BMW',4,'sedan','tata')
print(c.make_of_vehicle())
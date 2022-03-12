''''

class method:
    1) classmethod decoratore tells it is class method and you have to pass cls as a param in method
    2) you can not access instance variable without self in method param
    3) if you use self in classmethod while accessing it you have to pass the object
    4) you can not use self values in class method



static method:
    1) static method can be called without creating object
    2) if you pass self to static method it will throw an error


instance method:
    1) self is default for instance
'''

class Car:
    type_of_vehicle = 'Sedan'
    def __init__(self,name,cc):
        self.name = name
        self.cc = cc


    @classmethod
    def car_type(cls,self):
        return self.name

    @staticmethod
    def car_length(x,y):

        return x+y

    @staticmethod
    def car_type_cls(cls): #not possible
        return cls.type_of_vehicle


    def instance_logic(self):
        return self.name

c = Car('Tata',1200)
print(c.car_type(c)) #
print(c.car_length(2,3))

print(Car.car_length(3,4))

print(c.car_type_cls())
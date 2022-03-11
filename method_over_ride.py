class Vehicle():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def vehicle_type(self):
        return "i am {} from base class".format(self.type)


class CarHatchBack(Vehicle):

    def __init__(self, name, type, cc):
        super().__init__(name, type)

    def vehicle_type(self):
        return "i am {}".format(self.type)


c = CarHatchBack('bmw', 'sedan', 1200)
print(c.vehicle_type())

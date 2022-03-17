''''
encapulation is used to restrict data and to protect data
'''

class Computer:

    def __init__(self):
        self.__maxprice = 900
        self.minvalue = 200


    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c._Computer__maxprice =1
print(c._Computer__maxprice)



# print(c._avg_value) # you can access single underscore value using object
#
# #print(c.__maxprice) # you can not access double underscore value using object, error--> AttributeError: 'Computer' object has no attribute '__maxprice'
#
# # print(c.max_price()) # like this you can get the double underscore values
#
# c.__maxprice = 1000
# #c.max_price()
# print(c.__maxprice)
# # change the price
# # c.__maxprice = 1000
# # c.minvalue = 20
# # c.sellmin()
#
# # using setter function
# # c.setMaxPrice(1000)
# # c.sell()
#



''''
The Python interpreter rewrites any identifier with “__var” as “_ClassName__var”.
 And using this you can access the class member from outside as well
'''
# class Car:
#
#     def __init__(self,name,milage):
#
#         self.name = name
#         self._manufature = "TATA Group" #private
#         self.__owner = "Ratan Tata"
#         self.milage = milage
#
#     def owner_name(self):
#         return self.__owner
#
#
#
# car = Car("Tata",20)
# print(car.name)
# print(car._manufature)
# print(car._Car__owner) #mangled name
# print(car.owner_name())


class Computer:

    def __init__(self):
        self.__maxprice = 900
        self.minvalue = 200

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def sellmin(self):
        print("Selling  min Price: {}".format(self.minvalue))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.minvalue = 20
c.sellmin()

# using setter function
c.setMaxPrice(1000)
c.sell()

''''
Map function accepts list and tuple
it iterates each value and applies the logic on top of variable


'''
mr_data = ["Rohith Sharma","Virat Kohli","MS Dhoni","Sachin Tendulkar","Shiva"]
mrs_dara = ["Ritika Sajdeh","Anushka","Sakshi Dhoni","Anjali Tendulkar"]

pre_day = ("Sun","Mon","Tues")


def add_day(value):
    return value + "d@y"

def add_titile(data):
    return "Mr "+ data

if __name__ == '__main__':
    out_put = list(map(add_titile,mr_data))
    out_days = tuple(map(add_day,pre_day))
    print(out_days)


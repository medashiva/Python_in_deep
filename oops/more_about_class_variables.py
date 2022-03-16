class ClassVariable:

    my_var = 123
    def __init__(self):
        pass


cv_obj = ClassVariable()

print(cv_obj.my_var) # accessing class variable using object

print(ClassVariable.my_var) # we can access directly using class


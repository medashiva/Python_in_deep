'''
based on the inheritance methods will excute

'''
class A:

    def methodofa(self):
        return "method of A class"


class B():

    def methodofa(self):
        return "Method of B class"


class C(A,B):
    pass


c = C()
print(c.methodofa()) #method of A class



class D(B,A): #order based output
    pass

d = D()

print(d.methodofa()) #Method of B class

'''

Traceback (most recent call last):
  File "oops/multilevel_inheritance.py", line 14, in <module>
    class C(A,B): #C(A,B) throws error
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B


'''
class A:

    def methodofa(self):
        return "method of A class"


class B(A):

    def methodofa(self):
        return "Method of B class"


class C(B,A): #C(A,B) throws error
    pass


c = C()
print(c.methodofa()) #Method of B class




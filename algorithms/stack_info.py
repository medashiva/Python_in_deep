''''
reverse string using stack
'''
class Stack(object):

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        return None

    def pop(self):
        return self.items.pop()


    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.items):
            return False
        else:
            return True

    def return_stack(self):
        str = ''.join(self.items)
        return str



def reverse(strs):
    stack = Stack()
    mystr = ''
    for i in range(len(strs)):
        stack.push(strs[i])

    while not stack.is_empty():
        tem = stack.pop()
        mystr = mystr + tem

    return mystr

if __name__ == '__main__':
    c = reverse("shiva")
    print(c)

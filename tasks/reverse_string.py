if __name__ == '__main__':
    '''
    Approach 1
    '''
    c = "shiva"
    l = []
    for i in c:
        l.append(i)
    mystr = ''
    while not len(l) ==0:
        tem = l.pop()
        mystr = mystr + tem

    print(mystr)
    '''
        Approach 2
    '''
    length_of_string = len(c)
    new_str = ""
    increment = 1
    for i in range(0,length_of_string):
        new_str += c[length_of_string-increment]
        increment +=1

    print(new_str)
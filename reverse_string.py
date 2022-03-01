if __name__ == '__main__':
    c = "shiva"
    l = []
    for i in c:
        l.append(i)
    mystr = ''
    while not len(l) ==0:
        tem = l.pop()
        mystr = mystr + tem

    print(mystr)

''''


'''

numbers = [1,2,3,4,5,6,7,8,9]


def even_data(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':

    even_numbers = list(filter(even_data,numbers))

    print(even_numbers)
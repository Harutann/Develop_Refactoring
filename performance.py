from random import randint

def print_random1():
    base_list = [randint(0, 100000000) for i in range(1000000)]
    checked_list = [randint(0, 100000000) for i in range(100)]
    for temp in checked_list:
        if temp in base_list:
            print(f'temp:{temp} in a')


if __name__ == '__main__':
    print_random1()
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]. end=""))
            count = count + 1
            print()
    except OverflowError:
        print("IndexError: list index out of range")
    except (TypeError, ValueError, IndexError):
        print()
        return (count)

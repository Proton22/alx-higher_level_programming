#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = int a / int b
        print("{} / {} = {}".format(a, b, div))
    except ZeroDivisionError:
        print()
    finally:
        print("Inside result: {}".format(div))

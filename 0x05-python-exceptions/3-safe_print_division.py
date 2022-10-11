#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = int a / int b
        return div
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(div))

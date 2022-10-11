#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if value is None:
        return None
    i = 0
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False

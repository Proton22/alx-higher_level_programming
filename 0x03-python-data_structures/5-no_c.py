#!/usr/bin/python3
def no_c(my_string):
    y = list(my_string)
    for x in y:
        if x == 'c':
            y.remove('c')
        if x == 'C':
            y.remove('C')
    my_string = "".join(l)
    return my_string

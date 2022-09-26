#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a = t_a + (0, 0)
    t_b = t_b + (0, 0)
    list_a = list(t_a)
    list_b = list(t_b)
    list_c = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    return (tuple(list_c))

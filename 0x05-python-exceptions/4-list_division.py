#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = []
    my_list_2 = []
    count = 0
    i = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            return div
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
        return div

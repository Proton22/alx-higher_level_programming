#!/bin/python3
"""
    1-my_list: print list
"""


class list:
    """
       prints the list, but sorted.
       Method:
             print_sorted - prints the list in ascending order.
    """
    def print_sorted(self):
        """
            prints a list in ascending order.
        """
        print(sorted(self))

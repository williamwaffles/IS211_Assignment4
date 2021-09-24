import argparse
# other imports go here
import math
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


    
def sequential_search(a_list, num): # sequentially searches through a randomly generated list (a_list) to find a number (num)

    position = 0 # sets starting position of search
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == num:
            found = True
        else:
            position = position + 1
            return found

print(sequential_search(get_me_random_list(1000000),8))


def ordered_sequential_search(a_list,item):
    pass


def binary_search_iterative(a_list,item):
    pass
    
    
def binary_search_recursive(a_list,item):
    pass


if __name__ == "__main__":
    """Main entry point"""
    pass

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


def ordered_sequential_search(a_list, num):

    position = 0 # sets starting position of search
    found = False

    while position < len(a_list) and not found and not stop:
        if a_list[position] == num:
            found = True
        else:
            position = position + 1
            return found

#print(ordered_sequential_search(get_me_random_list(1000000),8))


def binary_search_iterative(a_list,num):

    first_num = 0
    last_num = len(a_list) - 1
    found = False

    while first_num <= last_num and not found:
        midpoint = int((first_num + last_num) / 2)
        if a_list[midpoint] == num:
            found = True
        else:
            if num < a_list[midpoint]:
                last_num = midpoint - 1
            else:
                first_num = midpoint + 1
    return found

#print(binary_search_iterative(get_me_random_list(1000000),8))

    
def binary_search_recursive(a_list, num):

    if len(a_list) == 0:
        return False
    else:
        midpoint = int(len(a_list) / 2)
        if a_list[midpoint] == num:
            return True
        else:
            if num < a_list[midpoint]:
                return binary_search_recursive((a_list[:midpoint], num)) # needs fixin'
            else:
                return binary_search_recursive((a_list[midpoint + 1], num)) # needs fixin'

print(binary_search_recursive(get_me_random_list(1000000),8))


if __name__ == "__main__":
    """Main entry point"""
    pass

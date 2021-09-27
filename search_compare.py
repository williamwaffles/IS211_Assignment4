import argparse
import time
import timeit
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


def ordered_sequential_search(a_list, num): # ordered sequential search of a list

    position = 0 # sets starting position of search
    found = False
    stop = False

    while position < len(a_list) and not found and not stop:
        if a_list[position] == num:
            found = True
        else:
            return found

def binary_search_iterative(a_list,num): # iterative binary search of a list

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

    
def binary_search_recursive(a_list, num): # recursive binary search of a list


    if len(a_list) == 0:
        return False
    else:
        midpoint = int(len(a_list) / 2)
        if a_list[midpoint] == num:
            return True
        else:
            if num < a_list[midpoint]:
                return binary_search_recursive((a_list[:midpoint]), num)
            else:
                return binary_search_recursive((a_list[midpoint + 1]), num)


if __name__ == "__main__":
    """Main entry point"""

    lists = [500, 1000, 5000]

    # Time check for the Sequential Search Function
    total_time_sequential = 0
    for list_size in lists:
        for i in range(100):
            new_list = get_me_random_list(list_size)
            start_time = time.time()
            sequential_search(new_list, -1)
            end_time = time.time()
            run_time = end_time - start_time
            total_time_sequential += run_time
            avg_run_time = total_time_sequential / 100
        print(f'The Sequential Search took an average of{avg_run_time:10.7f}s to search list size {list_size}!')
    print(f'Total Sequential Search run time: {total_time_sequential:10.7f}s')

    # Time check for the Ordered Sequential Search Function
    total_time_ordered = 0
    for list_size in lists:
        for i in range(100):
            new_list = get_me_random_list(list_size)
            sorted_new_list = sorted(new_list)
            start_time = time.time()
            ordered_sequential_search(sorted_new_list, -1)
            end_time = time.time()
            run_time = end_time - start_time
            total_time_ordered += run_time
            avg_run_time = total_time_ordered / 100
        print(f'The Ordered Sequential Search took an average of{avg_run_time:10.7f}s to search list size {list_size}!')
    print(f'Total Ordered Sequential Search run time: {total_time_ordered:10.7f}s')

    # Time check for the Iterative Binary Search
    total_time_iterative = 0
    for list_size in lists:
        for i in range(100):
            new_list = get_me_random_list(list_size)
            sorted_new_list = sorted(new_list)
            start_time = time.time()
            binary_search_iterative(sorted_new_list, -1)
            end_time = time.time()
            run_time = end_time - start_time
            total_time_iterative += run_time
            avg_run_time = total_time_iterative / 100
        print(f'The Iterative Binary search took an average of{avg_run_time:10.7f}s to search list size {list_size}!')
    print(f'Total Iterative Binary Search run time: {total_time_iterative:10.7f}s')

    # Time check for the Recursive Binary Search
    total_time_recursive = 0
    for list_size in lists:
        for i in range(100):
            new_list = get_me_random_list(list_size)
            sorted_new_list = sorted(new_list)
            start_time = time.time()
            binary_search_recursive(sorted_new_list, -1)
            end_time = time.time()
            run_time = end_time - start_time
            total_time_recursive += run_time
            avg_run_time = total_time_recursive / 100
        print(f'The Recursive Binary Search took an average of{avg_run_time:10.7f}s to search list size {list_size}!')
    print(f'Total Recursive Binary Search run time: {total_time_recursive:10.7f}s')
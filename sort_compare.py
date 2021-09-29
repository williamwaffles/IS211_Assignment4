import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list): # Insertion Sort Function

    start_time = time.time()
    for index in range(1, len(a_list)):

        currentvalue = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > currentvalue:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = currentvalue
    end_time = time.time() - start_time
    return end_time


def gapInsertionSort(a_list, start, gap):

    for i in range(start + gap, len(a_list), gap):

        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue

def shell_sort(a_list): # Shell sort function

    start_time = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:

        for start in range(sublistcount):
            gapInsertionSort(a_list, start, sublistcount)

        '''print("After increments of size", sublistcount,
              "The list is", a_list)'''

        sublistcount = sublistcount // 2
    end_time = time.time() - start_time
    return end_time


def python_sort(a_list): # Python's built-in sort function

    start_time = time.time()
    a_list.sort()
    end_time = time.time() - start_time
    return end_time


if __name__ == "__main__":
    """Main entry point"""

    lists =  [500, 1000, 2500]

    for list_size in lists:
        insertion_sort_time = 0.0
        shell_sort_time = 0.0
        python_sort_time = 0.0
        for i in range(0, 100):
            a_list = []
            for i in range(1, list_size):
                a_list.append(random.randint(1, 100))
            insertion_sort_time += insertion_sort(a_list)
            shell_sort_time += shell_sort(a_list)
            python_sort_time += python_sort(a_list)
        insertion_sort_avg = insertion_sort_time / 100
        shell_sort_avg = shell_sort_time / 100
        python_sort_avg = python_sort_time / 100
        print(f'Insertion Sort took an average of{insertion_sort_avg:10.7f}s to sort list size {list_size}!')
        print(f'Shell Sort took an average of {shell_sort_avg:10.7f}s to sort list size {list_size}!')
        print(f'Python Sort took an average of {python_sort_avg:10.7f}s to sort list size {list_size}!')
    print(f'Total Insertion Sort run time: {insertion_sort_time:10.7f}s')
    print(f'Total Shell Sort run time: {shell_sort_time:10.7f}s')
    print(f'Total Python Sort run time: {python_sort_time:10.7f}s')
import random
from order import *
"""
Given a list of n numbers, in this program, we are going to find the i_th smallest element of the list 
by means of divide and conquer strategy. We apply a "deterministic" algorithm to choose the pivot in each step
and then we partition the list around this pivot and go on recursively. 
This algorithm is very similar to the algorithm based of choosing pivots randomly 
and it has asymptotic running time of O(n) too.
"""
# random.seed(21)
# Generate a random list of numbers for testing
test_list = []
length = 100
for i in range(length):
    test_list.append(random.randint(1, 500))

# test_list = [12, 1, 8, 3, 2, 11, 7, 14, 19, 14]


def swap(my_list, pos1, pos2):
    x = my_list[pos1]
    my_list[pos1] = my_list[pos2]
    my_list[pos2] = x
    return my_list


def find_pivot_index(my_list):
    medians = []
    n = int(len(my_list)/5)
    for i in range(n - 1):
        temp = my_list[i*5:(i+1)*5]
        medians.append(median(temp))
    medians.append(median(my_list[(n - 1) * 5:]))
    pivot = dselect(medians, int((n+1)/2))
    pivot_index = my_list.index(pivot)
    return pivot_index


def dselect(my_list, i):
    n = len(my_list)
    if i > n:
        return False
    if n == 1:
        return my_list[0]
    # choosing the pivot index
    pivot_index = find_pivot_index(my_list)
    # end of choosing the pivot
    my_list = swap(my_list, 0, pivot_index)
    pivot = my_list[0]
    j = 0

    for k in range(1, n):
        if my_list[k] < pivot:
            j += 1
            my_list = swap(my_list, k, j)
    if j >= i:
        return dselect(my_list[1:j + 1], i)
    elif j + 1 == i:
        return pivot
    else:
        return dselect(my_list[j + 1:], i - j - 1)


# Testing
i = 50
sorted = merge_sort(test_list)
print(sorted)
ground_truth = sorted[i - 1]
computed = dselect(test_list, i)
print(ground_truth, computed, "   ", ground_truth == computed)

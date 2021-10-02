import random

"""
Given a list of n numbers, in this program, we are going to find the i_th smallest element of the list 
by means of divide and conquer strategy. We choose a "random" pivot and partition the list around this pivot
and recursively find the appropriate element in only of the partitions.
This algorithm is very similar to quick sort algorithm and has asymptotic running time of O(n).
"""
# random.seed(21)
# Generate a random list of numbers for testing
test_list = []
length = 100
for i in range(length):
    test_list.append(random.randint(1, 500))

# test_list = [12, 1, 8, 3, 2, 11, 7, 14, 19, 14]
# To count the number of swaps applied during the program
num_swap = 0


def swap(my_list, pos1, pos2):
    global num_swap
    x = my_list[pos1]
    my_list[pos1] = my_list[pos2]
    my_list[pos2] = x
    num_swap += 1
    return my_list


def rselect(my_list, i):
    n = len(my_list)
    if i > n:
        return False
    if n == 1:
        return my_list[0]
    pivot_index = random.randint(0, n - 1)
    my_list = swap(my_list, 0, pivot_index)
    pivot = my_list[0]
    j = 0

    for k in range(1, n):
        if my_list[k] < pivot:
            j += 1
            my_list = swap(my_list, k, j)
    if j >= i:
        return rselect(my_list[1:j + 1], i)
    elif j + 1 == i:
        return pivot
    else:
        return rselect(my_list[j + 1:], i - j - 1)


# We use merge sort to test our program
def merge(list1, list2):
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1

    while i < len(list1):
        combined_list.append(list1[i])
        i += 1

    while j < len(list2):
        combined_list.append(list2[j])
        j += 1

    return combined_list


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    half_length = int(len(my_list) / 2)
    first_half_sorted = merge_sort(my_list[:half_length])
    second_half_sorted = merge_sort(my_list[half_length:])
    return merge(first_half_sorted, second_half_sorted)


# Testing
i = 34
sorted = merge_sort(test_list)
print(sorted)
ground_truth = sorted[i - 1]
computed = rselect(test_list, i)
print(ground_truth, computed, "   ", ground_truth == computed)

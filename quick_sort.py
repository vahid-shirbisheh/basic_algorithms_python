import random

# random.seed(21)
"""
Here we implement the quick sort algorithm.
We choose the pivot numbers randomly using the built-in function in python shuffle.

"""
# Generate a random list of numbers for testing
test_list = []
length = 100
for i in range(length):
    test_list.append(random.randint(1, 50))

# test_list = [12, 1, 8, 3, 2, 11, 7, 14, 19, 14]


# To count the number of swaps applied during the program
num_swap = 0
# To keep track of pivots chosen during the program
pivots = []


def swap(my_list, pos1, pos2):
    global num_swap
    x = my_list[pos1]
    my_list[pos1] = my_list[pos2]
    my_list[pos2] = x
    num_swap += 1
    return my_list


def base_case(my_list, start, end):
    if start + 1 == end:
        if my_list[end] < my_list[start]:
            return swap(my_list, start, end)
        else:
            return my_list
    elif end < start:
        return my_list
    elif start == end:
        return my_list


def quick_sort(my_list, start, end):
    global pivots
    # The base cases:
    if end <= start + 1:
        return base_case(my_list, start, end)

    i = 0
    j = 0
    k = 0
    random_pivot_index = random.randint(start, end)
    swap(my_list, start, random_pivot_index)
    pivot = my_list[start]
    pivots.append(pivot)

    while start + j < end:
        j += 1
        if my_list[start + j] < pivot:
            i += 1
            swap(my_list, start + k + i, start + j)
        elif my_list[start + j] == pivot:
            k += 1
            swap(my_list, start + k + i, start + j)
            swap(my_list, start + k, start + k + i)

    my_list = my_list[:start] + my_list[start + k + 1:start + k + i + 1] + my_list[start:start + k + 1] + \
              my_list[start + k + i + 1:]


    # The left recursive call
    if i >= 0:
        my_list = quick_sort(my_list, start, start + i)
    # The right recursive call
    if start + k + i + 1 <= end:
        my_list = quick_sort(my_list, start + k + i + 1, end)

    return my_list


print("++++++++++++++++++++++++++++++++   The final result   ++++++++++++++++++++++++++++++++++++")
print("the original list: ", test_list)
sorted_list = quick_sort(test_list, 0, len(test_list) - 1)
print("The number of swaps: ", num_swap)
print("The number of pivots: ", len(pivots))
print("pivots: ", pivots)
print("The sorted list: ", sorted_list)

# If the list is not sorted properly ...
for i in range(length - 1):
    if sorted_list[i] > sorted_list[i + 1]:
        print("ERROR:    ", sorted_list[i], sorted_list[i + 1])

"""
We use this file as a quick reference for merge sort
and some other functions useful for testing or implementing other algorithms.
"""


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


def i_th_smallest(my_list, i):
    my_list = merge_sort(my_list)
    return my_list[i-1]


def median(my_list):
    return i_th_smallest(my_list, int((len(my_list) + 1) /2))

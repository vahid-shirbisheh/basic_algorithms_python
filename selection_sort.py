my_list = [3, 0, 7, 5, 9, 2, 4, 6, 8, 1]


def swap(my_list, m, n):
    temp = my_list[m]
    my_list[m] = my_list[n]
    my_list[n] = temp
    return my_list


def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)
    return lst


print(selection_sort(my_list))

my_list = [3, 0, 7, 5, 9, 2, 4, 6, 8, 1]


def swap(my_list, m, n):
    temp = my_list[m]
    my_list[m] = my_list[n]
    my_list[n] = temp
    return my_list


def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                swap(lst, j, j + 1)
    return lst


print(bubble_sort(my_list))

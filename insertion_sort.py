my_list = [3, 0, 7, 5, 9, 2, 4, 6, 8, 1]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while lst[j] > temp and j > -1:
            lst[j + 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


print(insertion_sort(my_list))

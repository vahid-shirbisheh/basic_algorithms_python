from order import *

my_list = [18, 31, 51, 78, 11, 2, 1, 0, 8, 9, 4, 7, -1, -2, 88, 13]
print(merge_sort(my_list))
print(i_th_smallest(my_list, 5))
print(f"The median of {my_list} is {median(my_list)}")


def find_pivot_index(my_list):
    medians = []
    n = int(len(my_list) / 5)
    for i in range(n - 1):
        temp = my_list[i * 5:(i + 1) * 5]
        print(temp)
        medians.append(median(temp))
    print(my_list[(n - 1) * 5:])
    medians.append(median(my_list[(n - 1) * 5:]))
    print(medians)
    pivot = i_th_smallest(medians, int((n + 1) / 2))
    pivot_index = my_list.index(pivot)
    return pivot_index


print(find_pivot_index(my_list))

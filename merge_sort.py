def merge(list1, list2):
    """
    :param list1: The first sorted list
    :param list2: The second sorted list
    :return: The sorted list consisting of elements of these sorted lists

    One notes that this function is slightly more general than what we actually need for merge sort!
    """
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


# Example for merging two sorted lists:
list_1, list_2 = [2, 4, 22, 23], [1, 5, 7, 11]
print(f"The combined sorted list consisting of elements of {list_1} and {list_2} is:")
print(merge(list_1, list_2))


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    half_length = int(len(my_list) / 2)
    first_half_sorted = merge_sort(my_list[:half_length])
    second_half_sorted = merge_sort(my_list[half_length:])
    return merge(first_half_sorted, second_half_sorted)


# Example for merge_sort function:
list_0 = [12, -10, 43, -1.2, 5, 4, 2, 105]
print(f"The sorted version of {list_0} is:")
print(merge_sort(list_0))

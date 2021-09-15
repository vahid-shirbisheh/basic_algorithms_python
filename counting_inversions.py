"""
Let A be a list of integer numbers. An inversion in A is a pair (A[i], A[j]) of elements of A
such that i<j but A[j]<A[i].


"""
def sort_merge_count_inversions(list1, list2):
    """
    :param list1: The first sorted list
    :param list2: The second sorted list
    :return: A pair consisting of a sorted list combining elements of these sorted lists
    and the number of split inversions between them.

    This function is in fact a modification of merge function used in merge sort algorithm.
    """
    combined_list = []
    i = 0
    j = 0
    num_split_inversions = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
            num_split_inversions += len(list1) - i

    while i < len(list1):
        combined_list.append(list1[i])
        i += 1

    while j < len(list2):
        combined_list.append(list2[j])
        j += 1

    return combined_list, num_split_inversions


# Example for merging and counting split inverrsions between two sorted lists:
list_1, list_2 = [2, 4, 22, 23], [1, 5, 7, 11]
combined_list, num_invs = sort_merge_count_inversions(list_1, list_2)
print(f"The combined sorted list consisting of elements of {list_1} and {list_2} is:  {combined_list}")
print(f"The number of split inversions between the lists {list_1} and {list_2} is:  {num_invs}")


def counting_inversions(my_list):
    if len(my_list) == 1:
        return my_list, 0

    half_length = int(len(my_list) / 2)
    first_half_sorted, num_inv1 = counting_inversions(my_list[:half_length])
    second_half_sorted, num_inv2 = counting_inversions(my_list[half_length:])
    combined_list_sorted, num_split_invs = sort_merge_count_inversions(first_half_sorted, second_half_sorted)
    return combined_list_sorted, num_split_invs + num_inv1 + num_inv2


# Example for merge_sort function:
list_0 = [9, 6, 12, 3, 10, 15, 7, 1, 13, 12]
sorted_list, num_invs = counting_inversions(list_0)
print(f"The sorted version of {list_0} is:")
print(sorted_list)
print(f"The number of inversions of {list_0} is:")
print(num_invs)

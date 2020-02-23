def MergeSort(list1):
    if len(list1) <= 1:
        return list1
    left_array = MergeSort(list1[:int(len(list1)/2)])
    right_array = MergeSort(list1[int(len(list1)/2):])

    return Merge(left_array, right_array)

def Merge(left_arr, right_arr):
    left_index, right_index = 0, 0
    sorted_array = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            sorted_array.append(left_arr[left_index])
            left_index += 1
        else:
            sorted_array.append(right_arr[right_index])
            right_index += 1

    if left_index != len(left_arr):
        while left_index < len(left_arr):
            sorted_array.append(left_arr[left_index])
            left_index += 1
    else:
        while right_index < len(right_arr):
            sorted_array.append(right_arr[right_index])
            right_index += 1

    return sorted_array

def arr_input():
    from random import randint
    list1 = []
    for i in range(100):
        list1.append(randint(0,100))

    print(list1)
    print(MergeSort(list1))

arr_input()
from random import randint
def QuickSort(input_array):
    if len(input_array) <= 1:
        return input_array
    less_than, equal, greater_than = [], [], []
    pivot = input_array[randint(0, len(input_array) - 1)]

    for element in input_array:
        if element < pivot:
            less_than.append(element)
        elif element > pivot:
            greater_than.append(element)
        else:
            equal.append(element)

    output = QuickSort(less_than) + equal + QuickSort(greater_than)
    return output

def call():
    input_array = []
    for i in range(1000):
        input_array.append(randint(0, 10000))
    print(input_array)
    print('Sorted: ', QuickSort(input_array))

call()
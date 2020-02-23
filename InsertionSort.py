def InsertionSort():
    ip = int(input('Enter number of elements: '))
    list1 = []
    for i in range(ip):
        list1.append(int(input('Enter element: ')))

    print('Original: ', list1)

    for i in range(1, len(list1)):
        integer_unsorted = list1[i]
        insert_index = i
        while (insert_index > 0 and list1[insert_index - 1] > integer_unsorted):
            list1[insert_index] = list1[insert_index - 1]
            insert_index = insert_index - 1
        list1[insert_index] = integer_unsorted
        print('Pass',i,' :',list1)
    print('Sorted: ', list1)

InsertionSort()
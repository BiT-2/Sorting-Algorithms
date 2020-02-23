def SelectionSort():
    ip = int(input('Enter number of elements: '))
    list1 = []
    for i in range(ip):
        list1.append(int(input('Enter element: ')))

    print('Original: ',list1)
    for i in range(len(list1) - 1):
        minimum = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[minimum]:
                minimum = j
        if minimum != i:
            temp = list1[i]
            list1[i] = list1[minimum]
            list1[minimum] = temp
        print('Pass', i, ' :', list1)


    print('Sorted: ', list1)

SelectionSort()


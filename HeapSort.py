class MaxHeap(object):
    def __init__(self, list1):
        self.heap_list = list1
        self.heap_size = len(list1) - 1
    def MaxHeapify(self, index):
        largest_index = index
        left_child = 2 * largest_index
        right_child = 2 * largest_index + 1
        if left_child <= self.heap_size and self.heap_list[left_child] > self.heap_list[largest_index]:
            largest_index = left_child
        if right_child <= self.heap_size and self.heap_list[right_child] > self.heap_list[largest_index]:
            largest_index = right_child
        if largest_index != index:
            self.heap_list[largest_index], self.heap_list[index] = self.heap_list[index], self.heap_list[largest_index]
            self.MaxHeapify(largest_index)

    def BuildMaxHeap(self):
        startIdx = self.heap_size // 2
        for i in range(startIdx, 0, -1):
            self.MaxHeapify(i)

    def ret_heap(self):
        return self.heap_list

    def max_child(self, index):
        if 2*index + 1 > self.heap_size:
            return 2*index
        else:
            if self.heap_list[2*index] > self.heap_list[2*index + 1]:
                return 2*index
            else:
                return 2*index + 1

    def balance_down(self, index):
        idx = index
        while 2*idx <= self.heap_size:
            max_child = self.max_child(idx)
            if self.heap_list[max_child] > self.heap_list[idx]:
                self.heap_list[max_child], self.heap_list[idx] = self.heap_list[idx], self.heap_list[max_child]
            idx = max_child


    def HeapSort(self):
        op_list = []
        while self.heap_size > 0:
            op_list.append(self.heap_list[1])
            self.heap_list[1] = self.heap_list[self.heap_size]
            self.heap_size = self.heap_size - 1
            self.heap_list.pop()
            self.balance_down(1)
        return op_list

def fn():
    list1 = [0, 1,3,2,5,4,7,6]
    h1 = MaxHeap(list1)
    h1.BuildMaxHeap()
    print(h1.HeapSort())
    print(h1.ret_heap())
fn()
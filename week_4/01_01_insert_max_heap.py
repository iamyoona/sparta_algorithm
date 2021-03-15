class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        if self.items == [None]:
            self.items.append(value)
        else:
            self.items.append(value)
            child_index = len(self.items) - 1

            while child_index // 2 >= 1:
                parent_index = child_index // 2
                print(child_index, parent_index)
                if self.items[parent_index] < self.items[child_index]:
                    self.items[parent_index], self.items[child_index] = self.items[child_index], self.items[parent_index]
                child_index = parent_index

        return self.items


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
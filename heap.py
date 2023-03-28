class MinBinaryHeap:

    def swap(self, first_pos, second_pos):
        self.heap[first_pos], self.heap[second_pos] = \
            self.heap[second_pos], self.heap[first_pos]

    @staticmethod
    def get_parent(pos):
        return (pos - 1) // 2

    @staticmethod
    def get_left_child(pos):
        return 2 * pos + 1

    @staticmethod
    def get_right_child(pos):
        return 2 * pos + 2

    def __init__(self):
        self.heap = []

    def __sift_down(self, pos):
        while 2 * pos + 1 < len(self.heap):
            left_pos = self.get_left_child(pos)
            right_pos = self.get_right_child(pos)
            j = left_pos
            if right_pos < len(self.heap) and self.heap[right_pos] < self.heap[left_pos]:
                j = right_pos
            if self.heap[pos] < self.heap[j]:
                break
            self.swap(pos, j)
            pos = j

    def __sift_up(self, pos):
        while self.heap[pos] < self.heap[self.get_parent(pos)]:
            self.swap(self.heap[pos], self.heap[self.get_parent(pos)])
            pos = (pos - 1) // 2

    def extract_min(self):
        if len(self.heap) == 0:
            raise ValueError("Empty heap")
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(len(self.heap) - 1)
        self.__sift_down(0)
        return temp

    def insert(self, value):
        self.heap.append(value)
        self.__sift_up(len(self.heap) - 1)


mb = MinBinaryHeap()
arr = [1, 3, 5, 2, 4, 6, 6, 5, 7, 12, 13, 14, 15]
for i in range(len(arr)):
    mb.insert(arr[i])

for i in range(len(arr)):
    print(mb.extract_min())




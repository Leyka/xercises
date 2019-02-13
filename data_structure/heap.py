"""
Min Binary heap : Parent node will always be smaller than its 2 children
Max heap is same than Min except root node has biggest number
ex.
     2
   /   \
  6    10
 / \  / \
90 8 30 70

arr[0]       => root
for i > 0
    arr[(i-1)/2] => parent node
    arr[(2*i)+1] => left child
    arr[(2*i)+2] => right child
"""


class MinHeap:
    def __init__(self):
        self.items = []

    def add(self, item: int):
        """ Add item to the heap """
        self.items.append(item)  # Item will be placed at the end
        self.heapify_up()

    def extract_root(self):
        """ Extract root element from the heap """
        # Replace root element by the last element then heapify down
        old_root = self.items[0]
        self.items[0] = self.items[self.last_index]
        self.items.remove(self.items[self.last_index])
        self.heapify_down()
        return old_root

    def heapify_up(self):
        """ Bottom-up scan: Starts with last item and check if child is smaller than parent.
        If it does, swap item with its parent and repeat process with the parent
        """
        index = self.last_index
        while self.has_parent(index) and self.items[index] < self.parent(index):
            self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def heapify_down(self):
        """ Top-down scan: Start with root item and check if value is greater than one of its child.
        If it does, swap parent and child. Now parent becomes the new child, repeat process with its new children.
         """
        index = 0
        while self.has_left_child(index):
            # Check which child (left or right) has the smallest number
            smaller_child_index = self.left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.right_child_index(index)
            if self.items[index] > self.items[smaller_child_index]:
                self.swap(index, smaller_child_index)
            else:
                break
            
            index = smaller_child_index

    def swap(self, idx1, idx2):
        tmp = self.items[idx1]
        self.items[idx1] = self.items[idx2]
        self.items[idx2] = tmp

    # ~ Helper methods/accessors ~

    @property
    def size(self):
        return len(self.items)

    @property
    def last_index(self):
        return self.size - 1

    def parent_index(self, idx):
        return int((idx - 1) / 2)

    def has_parent(self, idx):
        return self.parent_index(idx) >= 0

    def parent(self, idx):
        return self.items[self.parent_index(idx)]

    def left_child_index(self, idx):
        return 2 * idx + 1

    def has_left_child(self, idx):
        return self.left_child_index(idx) < self.size

    def left_child(self, idx):
        return self.items[self.left_child_index(idx)]

    def right_child_index(self, idx):
        return 2 * idx + 2

    def has_right_child(self, idx):
        return self.right_child_index(idx) < self.size

    def right_child(self, idx):
        return self.items[self.right_child_index(idx)]


# Test
heap = MinHeap()
heap.add(20)
heap.add(30)
heap.add(5)
heap.add(10)
assert(heap.size == 4)
assert(heap.extract_root() == 5 and heap.size == 3)
assert(heap.extract_root() == 10 and heap.size == 2)
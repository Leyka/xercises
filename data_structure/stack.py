"""
Stack => LIFO, vertical elements

- last inserted   |
-                 v next
- first inserted
"""
from node import Node


class Stack:
    def __init__(self):
        self.top = None  # top element
        self._size = 0

    @property
    def empty(self):
        return self.size == 0

    @property
    def size(self):
        return self._size

    @property
    def peek(self):
        if self.empty:
            raise Exception('Cannot peek an empty stack')
        return self.top.item

    def push(self, item):
        if self.empty:
            self.top = Node(item)
        else:
            old_top = self.top
            self.top = Node(item)
            self.top.next = old_top

        print('[push] {}'.format(item))
        self._size  += 1

    def pop(self):
        if self.empty:
            raise Exception('Cannot pop an empty stack')

        item = self.peek
        self.top = self.top.next
        self._size -= 1
        print('[pop] {}'.format(item))
        return item


# Test
s = Stack()
assert(s.size == 0 and s.empty)

s.push('Bob')
s.push('Alice')
s.push('Zelda')
assert(s.size == 3)
assert(s.peek == 'Zelda')

s.pop()
s.pop()
assert(s.size == 1)
assert(s.peek == 'Bob')
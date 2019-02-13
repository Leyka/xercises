"""
Queue => FIFO
enqueue -> |last node|node|...|first node| -> dequeue
                    <--next--

Note: next method is reversed compared to a classic linked list.
      this will be useful when dequeuing                   
"""
from node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    @property
    def empty(self):
        return self.size == 0

    @property
    def size(self):
        return self._size

    @property
    def peek(self):
        """ Returns first element value """
        if self.empty:
            raise Exception("Cannot peek an empty queue")
        return self.first.item 

    def enqueue(self, item):
        """ Add element at the beginning of the queue (rear) """
        if self.empty:
            self.first = self.last = Node(item)
        else:
            old_last = self.last
            self.last = Node(item)
            old_last.next = self.last

        self._size += 1
        print('[Enqueued] {}'.format(item))

    def dequeue(self):
        """ Delete element at the front of the queue """
        if self.empty:
            raise Exception('Cannot dequeue an empty queue')

        item = self.peek
        self.first = self.first.next
        self._size -= 1
        if self.empty:
            self.last = None
            
        print('[Dequeued] {}'.format(item))

    def print(self):
        if self.empty:
            print('[print] Queue is empty')
        else:
            print('Queue has {} elements:'.format(self.size))
            node = self.first
            print('[print] first >', end='')
            while node is not None:
                print('|{}'.format(node.item), end='')
                node = node.next
                if node is None: # End of queue
                    print('|< last')


# Test
q = Queue()
assert(q.size == 0 and q.empty)

q.enqueue(123)
q.enqueue(456)
q.enqueue('Bob')
assert(q.size == 3)
assert(q.peek == 123)

q.dequeue()
q.dequeue()
assert(q.size == 1)
assert(q.peek == 'Bob')

q.dequeue()
assert(q.empty)

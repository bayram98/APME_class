"""
Note that this implementation of the doubly linked list is simpler and, therefore, slightly
different from the one in the GTG book.
"""

class Node:
    def __init__(self, data, prev, next):
        self._data = data
        self._prev = prev
        self._next = next


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        len = 0
        walk = self._head
        while walk is not None:
            len += 1
            walk = walk._next
        return len

    def add(self, data):
        new_node = Node(data, None, None)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node._prev = self._tail
            new_node._next = None
            self._tail._next = new_node
            self._tail = new_node

    def remove(self, node_value):
        current_node = self._head
        while current_node is not None:
            if current_node._data == node_value:
                # if it's not the first element
                if current_node._prev is not None:
                    current_node._prev._next = current_node._next
                    current_node._next._prev = current_node._prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self._head = current_node._next
                    current_node._next._prev = None

            current_node = current_node._next

    def remove_first(self):
        self._head = self._head._next
        self._head._prev = None

    def remove_last(self):
        self._tail = self._tail._prev
        self._tail._next = None

    def insert_front(self, data):
        node = Node(data=data, next=self._head._next, prev=self._head)
        self._head._next._prev = node
        self._head._next = node

    def insert_last(self, data):
        node = Node(data=data, next=self._tail, prev=self._tail._prev)
        self._tail._prev._next = node
        self._tail._prev = node

    def insert(self, _value, _position=0, _previous=None, _next=None):
        if _value is None:
            raise ValueError('Cannot add None item to a list')
        if _position < 0:
            raise ValueError('Cannot add to negative position in the list')
        if _position == 0:
            if self._head:
                new_node = Node(_value, None, self._head)
                old_node = self._head
                self._head = new_node
                old_node._prev = new_node

            else:
                new_node = Node(_value, None, None)
                self._tail = new_node
                self._head = new_node
            return new_node
        else:
            current = self._head
            count = 0
            while current and ((count + 1) <= _position):
                # found the position to insert into or reached last item
                # if last item, insert at the end
                if (count + 1 == _position) or (count + 1 == self.__len__()):
                    node = Node(_value, current, current._next)
                    if current._next:
                        current._next._previous = node
                    current._next = node
                    return node
                else:
                    current = current._next
                    count += 1

    def print(self):
        current_node = self._head
        if current_node._next == None:
            print("List is empty")
        else:
            while current_node is not None:
                if current_node._next == None:
                    print(current_node._data, end="\n")
                else:
                    print(current_node._data, end=" ")
                current_node = current_node._next


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.add(5)
    d.add(6)
    d.add(50)
    d.add(30)
    d.print()
    d.remove(50)
    d.remove(5)
    d.print()

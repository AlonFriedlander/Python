class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("List is empty")
        popped_value = self.head.value
        self.head = self.head.next
        self._length -= 1
        return popped_value

    def head_value(self):
        if not self.head:
            return None
        return self.head.value

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0


ll = LinkedList()
print("Is empty?", ll.is_empty())  # Output: True

ll.push(1)
ll.push(2)
ll.push(3)
print("Head value:", ll.head_value())  # Output: 1

print("Length:", len(ll))  # Output: 3

print("Pop:", ll.pop())  # Output: 1
print("Head value after pop:", ll.head_value())  # Output: 2

print("Length after pop:", len(ll))  # Output: 2
print("Is empty after pop?", ll.is_empty())  # Output: False

# Simulating the memory
_memory = {}

def get_pointer(node):
    address = id(node)
    _memory[address] = node
    return address

def dereference_pointer(address):
    if address == 0:
        return None
    return _memory[address]

class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        new_node = Node(element)

        if self.head is None:
            # Empty list
            self.head = self.tail = new_node
        else:
            tail_ptr = get_pointer(self.tail)
            new_ptr = get_pointer(new_node)

            new_node.both = tail_ptr # new_node.both = tail XOR NULL
            self.tail.both ^= new_ptr # tail.both = prev XOR new
            self.tail = new_node

    def get(self, index):
        current = self.head
        prev_ptr = 0
        i = 0

        while current is not None and i < index:
            next_ptr = prev_ptr ^ current.both
            prev_ptr = get_pointer(current)
            current = dereference_pointer(next_ptr)
            i += 1

        if current is None:
            raise IndexError("Index out of bounds")

        return current
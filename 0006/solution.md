## Personal implementation attempt in Python

I've got to investigate about XOR linked lists since I didn't know about them but when I read about these I found a super interesting concept and a data structure that allows to save both pointers from a double linked list in only one value writing a new value bit to bit when both addresses got merged using the XOR logic gate and knowing one of the two pointers it's possible to retrieve the other pointer.

Since I'm working with Python, I tried to simulate the memory system that will let me have a relation between memory addresses and objects using a ```_memory``` variable. My personal approach implements a ```Node``` class that will have the value and the solely pointer from an XOR linked list:

```py
class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0
```

Because of the problem instructions I thought that working with Python would let me some predefined ```get_pointer``` and ```dereference_pointer``` functions. At least I got undefined function errors so maybe I misunderstood the problem's writing. I ended coding these functions trying to replicate an object's pointer using the Python ```id()``` function and dereferencing it with the previous mentioned memory structure:

```py
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
```

Then I used the ```Node``` class to now create a ```XORLinkedList``` class having an adding and getting functions. The first one checks the base case when the list is empty so then creates a new node that begins with the list. If the list already exists (if there's at least one element) then the new element is placed at the tail of the list and it is here in this case where both pointers are encoded into one single memory address.

In order to get the linked list, the get function iterates through the list decoding the next pointer since it already knows the current pointer value:

```py
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
```
Finally, it's possible to test the XOR linked list adding it up values and printing them back like:

```py
xor_list = XORLinkedList()
xor_list.add(24)
xor_list.add(8)
xor_list.add(30)
xor_list.add(81)

print(xor_list.get(0).value)
print(xor_list.get(1).value)
print(xor_list.get(2).value)
print(xor_list.get(3).value)
```
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        curr = self.head

        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


list = linkedlist()
list.append(1)
list.append(2)
list.append(3)
list.append(44)
list.append(55)

print("Original list:")
list.print()
list.reverse()
print("Reversed list:")
list.print()
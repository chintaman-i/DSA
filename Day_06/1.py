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

    def insert(self, new_node, pos):
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        p = 1
        temp = self.head
        while temp and p != pos - 1:
            temp = temp.next
            p += 1
            
        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        
        if temp.data == value:
            self.head = self.head.next
            return

        prev = None
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# --- Test Execution ---
list = linkedlist()
list.append(1)
list.append(2)
list.append(3)
list.append(44)
list.append(55)

print("Original list:")
list.print()

list.delete(99)

#print("\nDeleting 55:")
#list.delete(55)
#list.print()

list.delete(201)
list.print()
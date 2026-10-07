class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = val
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
        else:
            p = 1
            temp = self.head
            while(p != pos - 1 and temp.next != None):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def print(self):
        sum = 0
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            sum += 1
        print("count:", sum)


list = linkedlist()
n1 = node(1)
n2 = node(2)
n3 = node(3)

list.append(n2)
list.append(n3)
list.append(node(44))
list.append(node(55))

list.print()
list.insert(node(100), 2)
#list.print()
list.insert(node(200), 6)
list.print()

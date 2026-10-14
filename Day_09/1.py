class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head

   
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

        def insert(self, new_node, pos):
            if pos == 1:
                temp=self.head
                while(temp.next!=self.head):
                    temp=temp.next
                new_node.next=self.head
                self.head=new_node
                temp.next=self.head
            else:
                p=1
                temp=self.head
                while(p!=pos-1):
                    temp=temp.next

    def print(self):
        print()
        print("List of elements: ")
        temp=self.head
        while(True):
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break

list = linkedlist()
list.append(node(1))
list.append(node(2))
list.append(node(3))
list.append(node(44))
list.append(node(55))
list.print()
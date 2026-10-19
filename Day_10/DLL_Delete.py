class Node:
    
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node 
            new_node.prev=temp
        else:
            self.head=new_node

    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    def insert(self, new_node, pos): 
        temp = self.head 
        if pos == 1: 
            new_node.next = self.head 
            if self.head:
                self.head.prev = new_node 
            self.head = new_node 
        else: 
            p = 1 
            while p != pos - 1 and temp.next: 
                temp = temp.next 
                p += 1 
            
            new_node.next = temp.next 
            new_node.prev = temp 
            
            if temp.next: 
                temp.next.prev = new_node 
                
            temp.next = new_node 
             

    def delete(self,value):
        

list1=LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))
print("\nList of elements")
list1.print()

list1.insert(Node(100),2)
print("\nInsert")
list1.print()
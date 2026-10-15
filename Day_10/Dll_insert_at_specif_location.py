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

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
             




list1=LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))


list1.print()

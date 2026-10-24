class node:
    def __init__(self, value): 
        self.data = value 
        self.next = None 
class queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        print("Deleted node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            self.rear=None
            print("Queue is empty")
        temp=None

    def print(self):
        temp=self.front
        if self.front==None:
            self.rear=None
            print("Queue is empty")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next


q=queue()
q.enqueue(node(23))
q.enqueue(node(33))
q.enqueue(node(34))
q.enqueue(node(13))
q.print()

print("Afer Dequeue")
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print()



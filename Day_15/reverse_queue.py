class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            temp = self.top
            popped_data = temp.data
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print()

class queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        dequed_data = temp.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        temp = None
        return dequed_data

def reverse_stack(s1):
    q1 = queue()
    while not s1.is_empty():
        q1.enqueue(node(s1.pop()))
    
    while not q1.is_empty():
        s1.push(node(q1.dequeue()))
    s1.print()
#def reverse_queue(s1):



st = stack()
st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))
st.push(node(50))

print("Original Stack:")
st.print()

reverse_stack(st)


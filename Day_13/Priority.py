class Node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.front is None:
            self.front = self.rear = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return   

        temp = self.front
        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.rear = new_node
            

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(f"({temp.data},{temp.priority})",end=" ")
            temp = temp.next
        print("None")


pq = PriorityQueue()
pq.enqueue(Node(100, 2))
pq.enqueue(Node(1000, 1))
pq.enqueue(Node(150, 3))
pq.enqueue(Node(300, 4))

pq.display()

class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully")

    def display_next(self):
        if self.front is None:
            print("No patients waiting")
        else:
            print("\nNext Patient:")
            print("ID:", self.front.pid)
            print("Name:", self.front.name)
            print("Priority:", self.front.priority)

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Treated Patient:", self.front.name)
            self.front = self.front.next

    def display_all(self):
        if self.front is None:
            print("No patients waiting.")
        else:
            temp = self.front
            print("\nWaiting Patients:")
            while temp:
                print(temp.pid, temp.name, temp.priority)
                temp = temp.next

pq = PriorityQueue()

while True:
    print("\nHospital Emergency Management")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient (After Treatment)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority in [1, 2, 3]:
            pq.enqueue(pid, name, priority)
        else:
            print("Invalid Priority!")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
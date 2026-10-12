#concate two slls

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
            
    def delete(self, val): 
        if self.head is None: 
            print("List is empty") 
            return 
        temp = self.head 
        if temp.data == val: 
            self.head = self.head.next 
            return 
        prev = None 
        while temp: 
            if temp.data == val: 
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

    def concate(self,list2):
        temp=self.head
        while(temp.next):
            temp.next
        temp.next=list2.head

        



 
list = linkedlist() 
list.append(10) 
list.append(20) 
list.append(30) 
list.append(40) 
list.append(50) 
print("List1:") 
list.print() 

list2 = linkedlist() 
list2.append(11) 
list2.append(12) 
list2.append(13) 
list2.append(14) 
list2.append(15) 
print("List2:") 
list2.print() 

print("Concate")
list.concate(list2)
list.print()
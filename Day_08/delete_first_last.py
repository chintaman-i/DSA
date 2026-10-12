#delete first and last node of singly linked list

#delete the middle node
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
        
    def insert(self,new_node,pos): 
        if pos==0: 
            new_node.next=self.head 
            self.head=new_node 
            return 
        else: 
            p=0 
            temp=self.head 
            while(p!=pos-1): 
                temp=temp.next 
                p+=1 
            new_node.next=temp.next 
            temp.next=new_node 
            
    def print(self): 
        current = self.head 
        while current: 
            print(current.data, end=" ") 
            current = current.next 
        print() 
        
    def reverse(self): 
        prev=None 
        curr=self.head 
        while(curr): 
            next_node=curr.next 
            curr.next=prev 
            prev=curr 
            curr=next_node 
        self.head=prev 
        
    def sum_consecutive(self): 
        current=self.head 
        while current and current.next: 
            total=current.data+current.next.data 
            print(total,end=" ") 
            current= current.next 
        print() 
        
    def find_middle(self): 
        count=0 
        temp=self.head 
        while temp: 
            count+=1 
            temp=temp.next 
        mid=count//2 
        temp=self.head 
        for i in range(mid): 
            temp=temp.next 
        if temp: 
            print("middle node:",temp.data) 
        else: 
            print("list is empty") 

    def delete_middle(self):
        count = 0 
        temp = self.head 
        while temp: 
            count += 1 
            temp = temp.next 
            
        if count == 0:
            print("list is empty")
            return
        if count == 1:
            self.head = None
            return

        mid = count // 2 
        temp = self.head 
        prev = None
        for i in range(mid): 
            prev = temp
            temp = temp.next 
            
        prev.next = temp.next

    """def del_first_last(self):
        #temp=self.head
         while temp.next.next:
            temp=temp.next
        temp.next=None """
    
    def del_first_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None
    def del_alternate(self):
        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
        if prev:
            temp=prev.next


list = linkedlist() 
list.append(1) 
list.append(12) 
list.append(3) 
list.append(44) 
list.append(55) 

print("Original list:") 
list.print() 

#print("\nAfter deleting 12:") 
#list.delete(12) 
#list.print() 

print("\nAfter inserting 100 at position 1:") 
new_node = node(100) 
list.insert(new_node, 1) 
list.print() 

print("\nReversed list:") 
list.reverse() 
list.print() 

""" print("\nDeleting middle node:")
list.delete_middle()
list.print()

print("\nDeleting first and last node:")
list.del_first_last()
list.print() """

print("\nalternate")
list.del_alternate()
list.print()
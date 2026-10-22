class node:
      def __init__(self, value): 
        self.data = value 
        self.next = None 

class stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
            return  self.top is None

    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            temp=self.top
            print("Poped elemnts: ",temp.data)
            self.top=self.top.next
            temp=None

        

    def print(self):
        if self.is_empty():
             print("Stck is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

    def reverse(self):
        temp=self.top
        while temp:
            st1.push(node(temp.data))
            temp=temp.next

    def compare(self):




st=stack()
st1=stack()
st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))
st.push(node(50))
print("After Push")
st.print()
""" 
st.pop()

print("After Pop")
st.print() """
print("\nAfter Reverse")
st.reverse()
st1.print()
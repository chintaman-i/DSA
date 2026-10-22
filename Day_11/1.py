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

    def print(self):
        if self.is_empty():
             print("Stck is empty")
        else:
            print("Stack Contains: \n")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next


st=stack()
st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))
st.push(node(50))
st.print()

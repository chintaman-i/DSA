#Binary Search Tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None


    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                        

                elif new_node.data >=temp.data:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self,temp):
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)



btree=BST()
btree.insert(Node(10))
btree.insert(Node(20))
btree.insert(Node(25))
btree.insert(Node(30))
btree.insert(Node(45))
btree.insert(Node(50))

btree.inorder(btree.root)
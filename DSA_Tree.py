class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        
class Tree:
    def create_node(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
            
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    
    def traversal_inoder(self,root):
        if root is not None:
            self.traversal_inoder(root.left)
            print(root.data)
            self.traversal_inoder(root.right)
            
            

tree = Tree()
root= tree.create_node(5)
print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)
print("INorder ------------->>>>>>>>")
tree.traversal_inoder(root)
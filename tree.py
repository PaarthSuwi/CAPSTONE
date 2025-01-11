class tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.val, end=" ")  # Print the value of the node
        inorder_traverse(root.right)
    
def preorder_traverse(root):
    if root:
        print(root.val, end=" ")  # Print the value of the node
        preorder_traverse(root.left)
        preorder_traverse(root.right)
    
def postorder_traverse(root):
    if root:
        postorder_traverse(root.left)
        postorder_traverse(root.right)
        print(root.val, end=" ")  # Print the value of the node


root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)
root.left.right = tree(5)

print("Inorder Traversal:")
inorder_traverse(root) 

print("\nPreorder Traversal:")
preorder_traverse(root)

print("\nPostorder Traversal:")
postorder_traverse(root)   
        

#     1
#    / \
#   2   3
#  / \
# 4   5
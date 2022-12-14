class Node:
    def __init__(self,item):
        self.left= None
        self.right= None
        self.val=item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val), '->', end=' ')
        inorder(root.right)
        

def preorder(root):
    if root:
        print(str(root.val), '->', end=' ')
        preorder(root.left)
        preorder(root.right)
        
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val), '->', end=' ')

root= Node('A')
root.left= Node('D')
root.right= Node('Z')
root.left.left= Node('H')
root.left.right= Node('L')
root.left.right.left=Node('P')
root.right.right= Node('C')
root.right.right.right= Node('E')

print('Inorder traversal')
inorder(root)

print('\nPreorder traversal')
preorder(root)

print('\nPostorder traversal')
postorder(root)

        
        
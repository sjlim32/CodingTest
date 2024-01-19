import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, value = 0):
        self.item = value
        self.left = None
        self.right = None
        
    def node_value(self):
        return self.item
    
    def add_left(self,value):
        self.left = TreeNode(value)
        
    def add_right(self,value):
        self.right = TreeNode(value)
    
    def add_node(self, value) :
        if value < self.item:
            if self.left != None :
                self.left.add_node(value)
            else:
                self.add_left(value)
        else:
            if self.right != None :
                self.right.add_node(value)
            else:
                self.add_right(value)

def postorder_traversal(node):
    if node.left != None:
        postorder_traversal(node.left)
    
    if node.right != None:
        postorder_traversal(node.right)
    
    print(node.node_value())
    return

n = 0
first = 0
while n == 0:
    try:
        first = int(input())
        n+=1
    except:
        break

root = TreeNode(first)

while 1<= n <10000 :
    try : 
        push = int(input())
        root.add_node(push)
    except:
        break
    n+=1

if root.item != 0 :
    postorder_traversal(root)
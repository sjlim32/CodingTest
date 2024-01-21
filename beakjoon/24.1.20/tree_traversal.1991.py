# 이진 트리를 입력받고
# 전위 순회(preorder traversal)
# 중위 순회(inorder traversal)
# 후위 순회(postorder traversal)한 결과를 출력

import sys
# sys.setrecursionlimit(10**3)
input = sys.stdin.readline

class Tree:
  def __init__(self, input, lnode, rnode):
    self.left = lnode
    self.right = rnode
    self.data = input

def preorder(node):
    print(node.data, end = '')
    if node.left != '.':
      preorder(tree[node.left])
    if node.right != '.':
      preorder(tree[node.right])
        
def inorder(node):
    if node.left != '.':
      inorder(tree[node.left])
    print(node.data, end = '')
    if node.right != '.':
      inorder(tree[node.right])
        
def postorder(node):
    if node.left != '.':
      postorder(tree[node.left])
    if node.right != '.':
      postorder(tree[node.right])
    print(node.data, end = '')
    
level = int(input())
tree_input = []

for _ in range(level):
  x, y, z = input().split()
  tree_input.append([x, y, z])

tree = {}
for parent, lnode, rnode in tree_input:
  tree[parent] = Tree(parent, lnode, rnode)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])  



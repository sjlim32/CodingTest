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

## * Optimizing ##
# def preorder(root):
#   if root != '.':
#     print(root, end='')
#     preorder(tree[root][0])
#     preorder(tree[root][1])

# def inorder(root):
#   if root != '.':
#     inorder(tree[root][0])
#     print(root, end='')
#     inorder(tree[root][1])

# def postorder(root):
#   if root != '.':
#     postorder(tree[root][0])
#     postorder(tree[root][1])
#     print(root, end='')

# n = int(input())

# tree = dict()
# for i in range(n):
#   a, b, c = input().rstrip().split()
#   tree[a] = [b, c]

# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
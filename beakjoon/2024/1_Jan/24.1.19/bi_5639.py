
## ! Wrong Answer ##
import sys
input = sys.stdin.readline
# print = sys.stdout.readline
sys.setrecursionlimit(10**6)

n_left_list= set()


class Root():
  def __init__(self, temp):
    self.root = temp

class Node(Root):
  def __init__(self, temp):
    self.left = None
    self.right = None
    self.data = temp
    super().__init__(root)

  def insert_left(self, temp):
    self.left = Node(temp)
    print("input left", temp)
    n_left_list.add(temp)

  def insert_right(self, temp):
    for node in (n_left.list):
      if node.left < temp:
        node.left.right = temp


  def last_insert(self, temp):
    if self.data:
        if temp < self.data:
          if self.left is None:
            print("set left", temp)
            self.left = Node(temp)
          else:
            print("insert left", temp)
            self.left.insert(temp)

        elif temp > self.data:
          if self.right is None:
            print("set right", temp)
            self.right = Node(temp)
        else:
          print("insert right", temp)
          self.right.insert(temp)
    else:
      self.data = temp

  def insert(self, temp):
    if self.data:
      if temp < self.data:
        print("start left")
        self.insert_left(temp)
      elif self.data < temp and temp < self.root:
        print("start right")
        self.insert_right(temp)
      else:
        print("start last")
        self.last_insert(temp)

    else:
      self.data = temp

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()    
    if self.right:
      self.right.PrintTree()
    print(self.data)


# root = int(input)
# Root(root)
# Node(root)

# for i in sys.stdin:
#   root.insertion(int(i))

# root.PrintTree()

num_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]
root = num_list[0]

num = Node(root)
Root(root)

for i in num_list[1:]:
  # print(i)
  num.insert(i)

num.PrintTree()

# >> 트리가 5의 밑에서 무한 루프로 생성되게됨.


## ! Other Wrong Answer ##
# binary = [50, 30, 24, 5, 28, 45, 98, 52, 60]

# p = input()
# for i in p.split('\n'):
#   if i != '':
#     binary.append(int(i))

# binary = []

# for i in sys.stdin:
#   x = i.split('\n')
#   binary.append(int(x[0]))


# # 최소값 인덱스 검색 
# idx = binary.index(min(binary))



# # 인덱스 기준으로 분리
# root = binary[0]
# left = binary[1:idx+1]
# right = deque(binary[idx+1:])

# print(root, left, right)

# while True:
#   if any(n < root for n in binary):
#     print(left.pop())
#     if left:
#       print(right.popleft()) 
#       continue
    
#     else:
#       while right:
#         print(right.pop())
#       print(root)
#       break;


## ! OTHER ANSWER
# import sys
# input = sys.stdin.readline

# class TreeNode:
#     def __init__(self, value = 0):
#         self.item = value
#         self.left = None
#         self.right = None
        
#     def node_value(self):
#         return self.item
    
#     def add_left(self,value):
#         self.left = TreeNode(value)
        
#     def add_right(self,value):
#         self.right = TreeNode(value)
    
#     def add_node(self, value) :
#         if value < self.item:
#             if self.left != None :
#                 self.left.add_node(value)
#             else:
#                 self.add_left(value)
#         else:
#             if self.right != None :
#                 self.right.add_node(value)
#             else:
#                 self.add_right(value)

# def postorder_traversal(node):
#     if node.left != None:
#         postorder_traversal(node.left)
    
#     if node.right != None:
#         postorder_traversal(node.right)
    
#     print(node.node_value())
#     return

# n = 0
# first = 0
# while n == 0:
#     try:
#         first = int(input())
#         n+=1
#     except:
#         break

# root = TreeNode(first)

# while 1<= n <10000 :
#     try : 
#         push = int(input())
#         root.add_node(push)
#     except:
#         break
#     n+=1

# if root.item != 0 :
#     postorder_traversal(root)
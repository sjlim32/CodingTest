
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
# binery = [50, 30, 24, 5, 28, 45, 98, 52, 60]

# p = input()
# for i in p.split('\n'):
#   if i != '':
#     binery.append(int(i))

# binery = []

# for i in sys.stdin:
#   x = i.split('\n')
#   binery.append(int(x[0]))


# # 최소값 인덱스 검색 
# idx = binery.index(min(binery))



# # 인덱스 기준으로 분리
# root = binery[0]
# left = binery[1:idx+1]
# right = deque(binery[idx+1:])

# print(root, left, right)

# while True:
#   if any(n < root for n in binery):
#     print(left.pop())
#     if left:
#       print(right.popleft()) 
#       continue
    
#     else:
#       while right:
#         print(right.pop())
#       print(root)
#       break;
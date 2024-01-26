# 루트 없는 트리가 주어진다. 
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# n = 노드의 개수 ( 2 <= n <= 100,000 )
# 부모 노드의 번호를 n + 1 의 순서대로 출력

## ! Wrong Answer
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# if __name__ == '__main__':
#   n = int(input())
#   graph = dict.fromkeys(list(i for i in range(1, n + 1)), 0)

#   for _ in range (n-1):
#     x, y = map(int, input().split())
#     if x == 1:
#       graph[y] = x
#     elif y == 1 or graph[y] == 1:
#       graph[x] = y
#     elif graph[x] == 0:
#       graph[x] = y
#     else:
#       graph[y] = x

#   for i in range(1, n + 1):
#     if graph[i] != 0:
#       print(str(graph[i])+'\n')

###############################################################

import sys
input = sys.stdin.readline
print = sys.stdout.write

## ? My Answer ##

# sys.setrecursionlimit(10**6)
# node = int(input())
# graph = [ [] for _ in range(node + 1)]

# for _ in range(node-1):
#   x,y = map(int, input().split())
#   graph[x].append(y)
#   graph[y].append(x)

# parent = dict.fromkeys(list(i for i in range(1, node + 1)), 0)

# def dfs(myp, n, visited=set()):
#   parent[n] = myp
#   visited.add(n)

#   for adj in graph[n]:
#     if adj not in visited:
#       dfs(n, adj)


# if __name__ == '__main__':
#   dfs(0, 1)
#   for i in range(1, node + 1):
#     if parent[i] != 0:
#       print(str(parent[i])+'\n')


## * Optimizing ##
from collections import deque

if __name__ == '__main__':
  node = int(input())
  graph = [ [] for _ in range(node + 1)]

  for _ in range(node-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

  tree = [0] * (node + 1)
  q = deque([1])

  while q:
    v = q.popleft()

    for nv in graph[v]:
      if not tree[nv]:
        q.append(nv)
        tree[nv] = v

  for i in range(2, node + 1):
    print(f'{tree[i]}\n')
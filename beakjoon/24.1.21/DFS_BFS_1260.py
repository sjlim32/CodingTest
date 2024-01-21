# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**4 +1)

class Graph:
  def __init__(self, num_vertices):
    self.graph = {i: [] for i in range(1, num_vertices +1)}

  def add_edge(self, n, v):
    self.graph[n].append(v)
    self.graph[v].append(n)

    self.graph[n].sort()
    self.graph[v].sort()


vertex, edge, start = map(int, input().split())
g = Graph(vertex)

for _ in range(edge):
  edge = list(map(int, input().split()))
  g.add_edge(edge[0], edge[1])


def bfs(graph, start):
  if start not in graph:
    print(start)
    return

  visited = set()
  queue = deque([start])

  while queue:
    vertex = queue.popleft()

    if vertex not in visited:
      visited.add(vertex)
      print(vertex, end=' ')

      for node in graph[vertex]:
        if node not in visited:
          queue.append(node)


def dfs(graph, start, visited=None):
  if start not in graph:
    print(start)
    return

  if visited is None:
    visited = set()

  visited.add(start)
  print(start, end=' ')

  # 재귀 함수
  for next in graph[start]:
    if next not in visited:
      dfs(graph, next, visited)

print(g.graph)
dfs(g.graph, start)
print()
bfs(g.graph, start)

## * Optimizing ##
# import sys
# input = sys.stdin.readline

# def dfs(n):
#   visited[n] = True
#   dfs_list.append(n)
#   for w in sorted(adj_list(n)):
#     if not visited[w]:
#       dfs(w)

# def bfs(n):
#   visited[n] = True
#   queue = [n]

#   while queue:
#     v = queue.pop(0)
#     bfs_list.append(v)

#     for w in sorted(adj_list[v]):
#       if not visited[w]:
#         visited[w] = True
#         queue.append(w)

# node, edge, start = map(int, input().split())

# adj_list = [[] for _ in range(N + 1)]
# visited = [False] * (node + 1)

# for _ in range(edge):
#   a, b = map(int, input().split())
#   adj_list[a].append(b)
#   adj_list[b].append(a)


# dfs_list = []
# bfs_list = []

# dfs(start)
# visited = [False] * (node + 1)
# bfs(start)

# print(*dfs_list)
# print(*bfs_list)
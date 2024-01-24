# 첫째 줄에는 컴퓨터의 수가 주어진다. 
# 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

import sys
from collections import deque

input = sys.stdin.readline

# 노드의 수 = n, 간선의 수 = m
n = int(input())
m = int(input())
graph = [ [] for _ in range(n + 1) ]

for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

def bfs(start):
  q = deque([start])
  visited = set()

  while q:
    curr_node = q.popleft()
    visited.add(curr_node)
    for next_n in graph[curr_node]:
      if next_n not in visited:
        q.append(next_n)

  return visited

def dfs(node, visited=set()):
  visited.add(node)

  for next_n in graph[node]:
    if next_n not in visited:
      dfs(next_n)

  return visited

sys.stdout.write(str(len(bfs(1))-1))
# sys.stdout.write(str(len(dfs(1))-1))
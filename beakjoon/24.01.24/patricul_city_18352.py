# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 
# 모든 도로의 거리는 1이다.
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력

## ? My Answer ##

# 첫째 줄에 도시의 개수 N,
# 도로의 개수 M,
# 거리 정보 K,
# 출발 도시의 번호 X

# import sys
# from collections import deque, defaultdict

# input = sys.stdin.readline
# print = sys.stdout.write

# node, edge, short, start = map(int, input().split())

# INF = sys.maxsize

# graph = defaultdict(list)
# # distance = [ [INF] * (node + 1) for _ in range(node + 1)]
# distance = [ INF for _ in range(node + 1) ]

# for _ in range(edge):
#   begin, arrive = map(int, input().split())
#   graph[begin].append(arrive)

# def bfs(start):
#   q = deque([start])
#   distance[start] = 0
#   visited = set()

#   while q:
#     curr = q.popleft()
#     visited.add(curr)

#     if distance[curr] > short:
#       break

#     for next in graph[curr]:
#       if next not in visited:
#         if distance[curr] < distance[next]:
#           distance[next] = distance[curr] + 1
#         q.append(next)
#         distance[next] 

#   if short not in distance:
#     print('-1')

# if __name__ == "__main__":
#   bfs(start)
#   for i in range(node + 1):
#     print(str(i)+'\n') if short == distance[i] else None

## * Optimizing ##

# import sys
# from collections import deque

# input = sys.stdin.readline
# print = sys.stdout.write
# INF = sys.maxsize


# def dijkstra(graph, n, k ,start):
#   q = deque([])
#   q.append([start, 0])
#   dist = [ INF ] * (n + 1)
#   dist[start] = 0

#   res = []
#   while q:
#     curr, c_dist = q.popleft()
    
#     if c_dist > dist[curr]:
#       continue

#     if c_dist == k:
#       res.append(curr)
#       continue
    
#     for adj_n in graph[curr]:
#       cost = c_dist + 1

#       if cost < dist[adj_n]:
#         dist[adj_n] = cost
#         q.append([adj_n, cost])

#   return res

# def solution():
#     n, m, k, x = map(int, input().split())
#     graph = [[] for _ in range(n + 1)]

#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)

#     res = dijkstra(graph, n, k, x)

#     if res:
#         return "\n".join(map(str, sorted(res)))

#     return "-1"

# print(solution())

## * Optimizing2 ##

import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def bfs(start):
  INF = sys.maxsize
  distance = [ INF for _ in range(node + 1) ]  
  q = deque(start)
  distance[start] = 0
  visited = set()

  while q:
    curr = q.popleft()
    visited.add(curr)

    if distance[curr] > short:
      break

    for next in graph[curr]:
      if next not in visited:
        if distance[curr] < distance[next]:
          distance[next] = distance[curr] + 1
        q.append(next)
        distance[next] 
  
  res = []
  for i in range( node + 1 ):
    if distance[i] == short:
      res.append(i)
  
  return res

if __name__ == "__main__":
  node, edge, short, start = map(int, input().split())
  graph = [ [] for _ in range(node + 1) ]

  for _ in range(edge):
    begin, arrive = map(int, input().split())
    graph[begin].append(arrive)

  res = bfs(start)
  if res:
    print("\n".join(map(str, sorted(res))))
  else:
    print("-1")
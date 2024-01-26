import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF] * (n+1) 

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def get_min_node():
  min_dis = INF
  idx = 0
  for node in range(1, n + 1):
    if distance[node] < min_dis and not visited[node]:
      min_dis = distance[node]
      idx = node
  return idx

start, end = map(int, input().split())

def dijkstra_V2(start):
  distance[start] = 0
  visited[start] = True

  for node, dist in graph[start]:
      distance[node] = dist

  for _ in range(n-1):
    curr = get_min_node()
    visited[curr] = True

    for nx_node, nx_dist in graph[curr]:
      distance[nx_node] = min(distance[nx_node], distance[curr] + nx_dist)
      # new_dist = nx_dist + distance[curr]
      # if new_dist < distance[nx_node]:
      #   distance[nx_node] = new_dist


dijkstra_V2(start)

print(distance)
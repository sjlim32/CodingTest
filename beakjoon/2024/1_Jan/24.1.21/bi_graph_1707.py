import sys
from collections import deque, defaultdict

## * Optimizing

input = sys.stdin.readline
sys.setrecursionlimit(10**4 +1)

# bfs 탐색 
def bfs(x, g, color):
  q = deque([x])

  while q:
    now = q.popleft()
    # 다음컬러 = 내 컬러가 1이면 2, 2이면 1
    next_color = color[now] % 2 + 1

  # 1 ~ v+1 까지 q에 순차적으로 들어옴
  # 정점 g에 대한 인접 정점 모두 확인
  # 다음 인접 정점이 색이 없다면, now와 다른 색을 추가하고 q에 넣음
    for next in g[now]:
      if not color[next]:
        color[next] = next_color
        q.append(next)

  # 만약 다음 인접 정점이 색이 있는데, now와 같은색을 가지고 있다면 false 리턴
      elif color[next] != next_color:
        return False
        break

  return True

def sol():
  v, e = map(int, input().split())
  color = [0] * (v+1)
  # default가 list 형식인 딕셔너리 생성
  g = defaultdict(list)

  # 양방향 리스트 생성
  for _ in range(e):
    x,y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)

  # 정점의 범위 1 ~ v+1 까지 탐색
  for j in range(1, v+1):

  # color가 모두 있으면 "YES" 리턴
    if color[j]:
      continue

    color[j] = 1

  # 생성한 리스트 g에 대해서 j(1 ~ v+1) 범위 탐색
  # 현재 정점 j에 대한 인접 정점 중 j와 같은 색을 가지고 있다면 "NO" 리턴
    if bfs(j, g, color) == False:
      return "NO"
      
  return "YES"

if __name__ == "__main__":
  tc = int(input())

  for _ in range(tc):
    print(sol())


## First Answer
# input = sys.stdin.readline
# sys.setrecursionlimit(10**4 +1)

# class Graph:
#   def __init__(self, num_vertices):
#     self.graph = {i: [] for i in range(1, num_vertices +1)}

#   def add_edge(self, n, v):
#     self.graph[n].append(v)
#     self.graph[v].append(n)

# def bfs(x, g, color):
#   q = deque([x])

#   while q:
#     now = q.popleft()
#     next_color = color[now] % 2 + 1

#     for next in g[now]:
#       if not color[next]:
#         color[next] = next_color
#         q.append(next)

#       elif color[next] != next_color:
#         return False
#         break

#   return True

# # 그래프 만들기
# tc = int(input())
# tc_list = []

# for _ in range(tc):
#   vertex, edge= map(int, input().split())
#   g = Graph(vertex)

#   for _ in range(edge):
#     edge = list(map(int, input().split()))
#     g.add_edge(edge[0], edge[1])

#   tc_list.append(g)


# # 그래프 탐색, 색칠
# def sol(g):
#   color = [0] * (len(list(g.graph.keys()))+1)

#   for j in range(1, len(color)):

#     if color[j]:
#       continue

#     color[j] = 1

#     if bfs(j, g.graph, color) == False:
#       return "NO"
      
#   return "YES"

# for i in (tc_list):
#   print(sol(i))
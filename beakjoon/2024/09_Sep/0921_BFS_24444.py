# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. 
# i번째 줄에는 정점 i의 방문 순서를 출력한다. 
# 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start: int):
  count = 1
  q = deque()
  q.append(start)
  visited[start] = count

  while(q):
    v = q.popleft()

    for e in graph[v]:
      if visited[e] == 0:
        q.append(e)
        count+=1
        visited[e] = count


if __name__ == "__main__":
  vertex, edge, start = map(int, input().split())
  graph = [[] for _ in range(vertex + 1)]
  visited = [0] * (vertex + 1)

  for _ in range(edge):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

  for i in graph:
    i.sort()

  dfs(start)

  for i in range(1, vertex + 1):
    print(visited[i])

  
#####* OPTIMIZING *#####

# from collections import deque
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M, R = map(int, input().split())
#     graph = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         start, end = map(int, input().split())
#         graph[start].append(end)
#         graph[end].append(start)
#     orders = [0 for _ in range(N + 1)]
#     visited = [False for _ in range(N + 1)]

#     queue = deque([R])
#     visited[R] = True
#     order = 1
#     orders[R] = order
#     while queue:
#         node = queue.popleft()
#         graph[node].sort()
#         for v in graph[node]:
#             if not visited[v]:
#                 visited[v] = True
#                 queue.append(v)
#                 order += 1
#                 orders[v] = order

#     print(*orders[1:], sep="\n")

# if __name__=="__main__":
#     solution() 


# 5 5 1
# 1 4
# 1 2
# 2 3
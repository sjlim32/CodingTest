# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)

# def dfs(node: int, graph: list[list], visited: dict[int, int]) -> None:
#   global index
#   if node in visited:
#     return;

#   visited[node] = index
#   graph[node].sort()

#   for v in graph[node]:
#     if v not in visited:
#       index += 1
#       dfs(v, graph, visited)

# if __name__ == "__main__":
  
#   vertex, edge, start = map(int, input().split())
#   graph = list([] for _ in range(vertex + 1))
#   visited = defaultdict(int)
#   index = 1
  
#   for _ in range(edge):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)

#   dfs(start, graph, visited)
#   print(f"{visited}\n")
#   for i in range(1, vertex + 1):
#     if visited[i]:
#       print(f"{visited[i]}\n")
#     else:
#       print("0\n")

############* OPTIMIZING *############
if __name__ == "__main__":
  vertex, edge, start = map(int, input().split())
  visited = [0] * (vertex + 1)
  
  graph_dict = defaultdict(list)
  for _ in range(edge):
    s, e = map(int, input().split())
    graph_dict[s].append(e)
    graph_dict[e].append(s)

  ########? Stack ?########
  order = 0
  stack = [start]
  while stack:
    node = stack.pop()
    if visited[node]:
      continue

    order += 1
    visited[node] = order

    for next_node in sorted(graph_dict[node], reverse=True):
      if visited[next_node] == 0:
        stack.append(next_node)

  ########? print ?########
  for visited_node in visited[1:]:
    print(f"{visited_node}\n")
    
# e.g : result = 1 2 3 4 0
# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4

# e.g : result = 1 2 3 4 5
# 5 6 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4
# 5 1

# e.g : result = 3 2 5 1 6 4
# 6 8 4
# 1 6
# 1 2
# 2 6
# 2 3
# 2 4
# 3 5
# 4 5
# 3 4


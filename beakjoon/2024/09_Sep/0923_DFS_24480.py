# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. 
# i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 
# 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start: int):
  global count
  visited[start] = count
  count += 1

  for edge in graph[start]:
    if visited[edge] == 0:
      dfs(edge)

if __name__ == "__main__":
  v, e, s = map(int, input().split())
  graph = [[] for _ in range(v + 1)]
  visited = [0] * (v + 1)
  count = 1
  
  for _ in range(e):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

  for i in graph:
    i.sort(reverse = True)

  dfs(s)

  for j in range(1, v + 1):
    print(visited[j])
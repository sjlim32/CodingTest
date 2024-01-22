# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

#첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# BFS - 큐 활용 (선입선출)

import sys
from collections import deque
input = sys.stdin.readline

# def bfs (graph, node, visited):
#   queue = deque([node])
#   # 현재 노드 방문처리
#   visited[node] = True

#   # 큐가 빌 때까지 반복
#   while queue:
#     # 삽입된 노드 하나 꺼내기
#     v = queue.popleft()
#     # 탐색 순서 출력
#     print(v, end= ' ')

#     # 현재 처리 중인 노드에서 방문하지 않은 인접 노드 모두 큐에 삽입
#     for i in graph[v]:
#       if not (visited[i]):
#         queue.append(i)
#         visited[i] = True


# if __name__ == "__main__":
#   input()

#   visited = [False] * 9
#   bfs(graph, 1, visited)

n, m = map(int, input().split())
maze = []

for _ in range(n):
  maze.append(list(map(int, list(input().strip('\n')))))

print(maze)

def BFS():
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque([(0, 0, 1)])
  visited = set([(0, 0)])

  while q:
    x, y, dist = q.popleft()

    if x == n - 1 and y == m - 1:
      return str(dist)

    for i in range(4):
      fx = x + dx[i]
      fy = y + dy[i]
    
      if 0 <= fx < n and 0 <= fy < m and (fx, fy) not in visited:
        if maze[fx][fy] == 1:
          visited.add((fx, fy))
          q.append((fx, fy, dist + 1))


# print(BFS())
sys.stdout.write(BFS())
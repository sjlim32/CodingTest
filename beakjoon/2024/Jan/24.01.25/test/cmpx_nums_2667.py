# <그림 1>과 같이 정사각형 모양의 지도가 있다. 
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 

# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


# 첫 번째 줄에는 지도의 크기 N, 5 <= N <= 25
# N 줄에는 N 개의 자료 = 0 or 1

## ? My Answer ##
from collections import deque

def BFS(sc, sr):
  building = 0
  ## ! Optimizing ##
  # dy = [1, -1, 0, 0]
  # dx = [0, 0, 1, -1]
  d = [(0,1), (0,-1), (1,0), (-1,0)]

  q = deque([])
  q.append([sc, sr])

  while q:
    y, x = q.popleft()
    if complexs[y][x] == 1:
      complexs[y][x] = -1
      building += 1

    ## ! Optimizing ##
    # for i in range(4):
    #   fy = y + dy[i]
    #   fx = x + dx[i]
    for dy, dx in d:
      fy, fx = y + dy, x + dx
      if 0 <= fy < n and 0 <= fx < n and complexs[fy][fx] == 1 and [fy, fx] not in q:
        q.append([fy, fx])
      

  if building > 0:
    result.append(building)


if __name__ == '__main__':
  n = int(input())
  complexs = [ list(map(int, input())) for _ in range(n) ]
  result = []
  for y in range(n):
    for x in range(n):
      if complexs[y][x] == 1:
        BFS(y ,x)

  print(len(result))
  result.sort()
  for i in result:
    print(i)

## * Optimizng ##
# import sys
# sys.setrecursionlimit(100000)

# N = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

# d = [(0,1), (0,-1), (1,0), (-1,0)]
# def dfs(x, y, cnt):
#     graph[y][x] = 0
#     for dx, dy in d:
#         X, Y = x + dx, y + dy
#         if (0 <= X < N) and (0 <= Y < N) and graph[Y][X]:
#             cnt = dfs(X, Y, cnt+1)
#     return cnt
          
# cnt = []

# for y in range(N):
#     for x in range(N):
#         if graph[y][x]:
#             cnt.append(dfs(x, y, cnt=1))

# cnt.sort()
# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])
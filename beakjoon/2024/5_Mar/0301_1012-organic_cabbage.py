# 고랭지에서 유기농 배추를 재배
# 배추흰지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호
# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호
# 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해 
# 첫째 줄에는 배추밭의 가로길이 M(1 ≤ M ≤ 50), 세로길이 N(1 ≤ N ≤ 50), 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
# 두 배추의 위치가 같은 경우는 없다.

# import sys
# from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write

# def solution() -> None:
#   column, row, init_cab = map(int, input().split())
#   cab_field = list([0] * row for _ in range(column))

#   for _ in range (init_cab):
#     y, x = map(int, input().split())
#     cab_field[y][x] = 1

#   worm = 0
#   for y in range(column):
#     for x in range(row):
#       if cab_field[y][x] != 0:
#         worm += 1
#         bfs(y, x, cab_field)

#   print(f"{worm}\n")
  

# def bfs(y: int, x: int, cab_field: list[list]) -> None:
#   queue = deque([[y, x]])
#   col, row = len(cab_field), len(cab_field[0])

#   while queue:
#     ny, nx = queue.popleft()

#     if cab_field[ny][nx] == 0:
#       continue
    
#     cab_field[ny][nx] = 0

#     for i in range(4):
#       mx, my = nx + fx[i], ny + fy[i]
#       if (mx >= 0 and mx < row) and (my >= 0 and my < col):
#         if cab_field[my][mx] != 0:
#           queue.append([my, mx])

# if __name__ == "__main__":
#   fx = [0, 1, 0, -1]
#   fy = [1, 0, -1, 0]

#   test_case = int(input())

#   for _ in range(test_case):
#     solution()

############* OPTIMIZING *############

import sys
input = sys.stdin.readline
print = sys.stdout.write

def bfs(x: int, y: int, cab_field: list[list]) -> None:
  queue = [(x, y)]
  cab_field[x][y] = 0

  while queue:
    x, y = queue.pop(0)

    for i in range(4):
      nx = x + fx[i]
      ny = y + fy[i]

      if nx < 0 or nx >= row or ny < 0 or ny >= column:
        continue

      if cab_field[nx][ny] == 1:
        queue.append((nx, ny))
        cab_field[nx][ny] = 0


if __name__ == "__main__":
  fx = [1, -1, 0, 0]
  fy = [0, 0, 1, -1]

  test_case = int(input())

  for _ in range(test_case):
    row, column, init_cab = map(int, input().split())
    cab_field = list([0] * column for _ in range(row))

    for _ in range (init_cab):
      x, y = map(int, input().split())
      cab_field[x][y] = 1

    worm = 0
    for x in range(row):
      for y in range(column):
        if cab_field[x][y] != 0:
          worm += 1
          bfs(x, y, cab_field)

    print(f"{worm}\n")



# e.g : result = 5 1
# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# 1
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
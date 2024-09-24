# ‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
# ‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
# ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
# ‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
# ‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

# 무조건 x += 1, y += 1 로 이동
# 이동한 칸에 쓰여있는 숫자만큼만 이동 가능

goal = int(input())
matrix = [list(map(int, input().split())) for _ in range(goal)]
visited = [[0]*goal for _ in range(goal)]

def dfs(x: int, y: int):
  if x < 0 or x >= goal or y < 0 or y >= goal or visited[x][y]:
    return
  
  if matrix[x][y] == -1:
    visited[x][y] = 1
    return

  visited[x][y] = 1
  
  dfs(x + matrix[x][y], y)
  dfs(x, y + matrix[x][y])

dfs(0, 0)

if visited[-1][-1]:
  print("HaruHaru")
else:
  print("Hing")
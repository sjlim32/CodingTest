dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x:int, y:int, nums:str):
  if len(nums) == 6:
    res.add(nums)
    return;

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 5 and 0 <= ny < 5:
      dfs(nx, ny, nums + matrix[nx][ny])


matrix = [input().split() for _ in range(5)]
res = set()

for i in range(5):
  for j in range(5):
    dfs(i, j, matrix[i][j])

print(len(res))

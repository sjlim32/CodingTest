# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

import sys

n = int(input())
colors = []

for _ in range(n):
  r, g, b = [*map(int, input().split())]
  colors.append([r, g, b])

dp = [ [0] * 3 for _ in range(n)]
dp[0] = [i for i in colors[0] ]

for i in range(1, n):
  r, g, b = colors[i]
  
  for j in range(3):
    if j == 0:
      dp[i][j] = min(dp[i-1][1] + r, dp[i-1][2] + r)
    if j == 1:
      dp[i][j] = min(dp[i-1][0] + g, dp[i-1][2] + g)
    if j == 2:
      dp[i][j] = min(dp[i-1][0] + b, dp[i-1][1] + b)

print(min(dp[n-1]))

## * Optimizing ##
# import sys
# input = sys.stdin.readline

# N = int(input())
# RGB = [0] * 3
# for _ in range(N):
#     r, g, b = map(int, input().split())
#     RGB = [r + min(RGB[1], RGB[2]), g + min(RGB[0], RGB[2]), b + min(RGB[0], RGB[1])]
# print(min(RGB))
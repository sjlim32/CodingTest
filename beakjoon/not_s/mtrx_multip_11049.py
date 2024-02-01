# 첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.
# 둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)
# 항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
  x, y = map(int, input().split())
  nums.append([x, y])


n_nums = []
print(nums)

for i in range(n-1):
  x, y, z = nums[i][0], nums[i+1][0], nums[i+1][1]
  n_nums.append([x, y, z])

print(n_nums)
import sys
input = sys.stdin.readline
print = sys.stdout.write

seq, board= [], set()

r = int(input())

for _ in range (r):
  nums = list(map(int, input().split()))
  seq.append(nums)
              
ans = [0 for _ in range(r)]

for idx, (x, y, fx, fy) in enumerate(reversed(seq)):
  start = [x, y]

  for zx in range(x, fx + x):
    for zy in range (y, fy + y):
      if (zx, zy) not in board:
        board.add((zx, zy))
        ans[idx] += 1
        
for answer in reversed(ans):
  print(f"{answer}\n")


# OPTIMIZING

import sys
input = sys.stdin.readline
print = sys.stdout.write

seq, board = [], [[0] * 1001 for _ in range(1001)]

r = int(input())

for _ in range (r):
  nums = list(map(int, input().split()))
  seq.append(nums)

for idx, (x, y, fx, fy) in enumerate(seq):
  start = [x, y]

  for zx in range(x, fx + x):
    for zy in range (y, fy + y):
        board[zx][zy] = idx + 1
        
for i in range(1, r + 1):
  count = 0
  for row in board:
    count += row.count(i)
  print(f"{count}\n")


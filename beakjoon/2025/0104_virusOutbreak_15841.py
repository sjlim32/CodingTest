# 1 - 1
# 2 - 1
# 3 - 2 (1)
# 4 - 3 (2)
# 5 - 5 (3)
# 6 - 8 (5)
# 7 - 13 (8)
# 8 - 21 (13)
# 9 - 34 (21)
# 10 - 55 (34)
# 11 - 89 

list = [0 for _ in range(491)]
list[1], list[2] = 1, 1

def fibonacci(n: int) -> int:
  if n < 3:
    return 1
  else:
    if list[n - 1] == 0:
      list[n-1] = fibonacci(n - 1)
    if list[n - 2] == 0:
      list[n - 2] = fibonacci(n - 2)
    return list[n - 2] + list[n - 1]
    
while True:
  n = int(input())
  if n == -1:
    break
  print(f"Hour {n}: {fibonacci(n)} cow(s) affected")


# OPTIMIZING

import sys

dp = [0]*491
dp[1] = 1
for i in range(2, 491):
    dp[i] = dp[i-1] + dp[i-2]
while True:
    X = int(sys.stdin.readline())
    if X == -1:
        break
    print(f'Hour {X}: {dp[X]} cow(s) affected')
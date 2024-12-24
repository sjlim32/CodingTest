import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
sum = 0
for _ in range(n):
  l, w, d, k = map(float, input().split())
  if ((l <= 56.0 and w <= 45.0 and d <= 25.0) or (l + w + d <= 125.0)) and k <= 7.0:
    print("1\n")
    sum += 1
  else:
    print("0\n")
print(f"{sum}")

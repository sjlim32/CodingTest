n = int(input())

for _ in range (n):
  x = input().split()
  y = x[2:] + x[:2]
  print(" ".join(y))

# OPTIMIZING

for _ in range(int(input())):
  str = list(input().split())
  print(' '.join(str[2:]), str[0], str[1])
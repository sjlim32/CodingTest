n, m = map(int, input().split())
s = input()
list = []

for _ in range(m):
  list.append(input())

for post in list:
  i = 0
  for x in post:
    if i >= n:
      break;
    if s[i] == x:
      i += 1
  if i == n:
    print("true")
  else:
    print("false")

# import sys 
# input = sys.stdin.readline
# print = sys.stdout.write

# N, M = map(int, input().split())
# s = input()

# for _ in range(M):
#   post_it = input().strip()
#   i = 0
  
#   for x in post_it:
#     if 1 >= N:
#       break;
#     if s[i] != x:
#       continue
#     i += 1

#   if i == N:
#     print("true\n")
#   else:
#     print("false\n")

# OPTIMIZING
import sys 
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
s = input().strip()

for _ in range(M):
  post_it = input().strip()
  i, x = 0, 0
  
  while 0 < N - i <= len(post_it) - x:
    if s[i] == post_it[x]:
      i += 1
    x += 1

  print("true\n" if i == N else "false\n")
  
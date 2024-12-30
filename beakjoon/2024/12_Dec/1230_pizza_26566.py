# 3
# 8 4
# 7 9
# 9 2
# 4 7
# 841 108
# 8 606

for _ in range(int(input())):
  s, p1 = map(int, input().split())
  w, p2 = map(int, input().split())

  if s/p1 >= w**2*3.14/p2:
    print("Slice of pizza")
  else:
    print("Whole pizza")
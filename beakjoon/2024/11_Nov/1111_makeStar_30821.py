vtx = int(input())
star = 1
for i in range(vtx, (vtx-5), -1):
  star= star * i
print(star//120)

# OPTIMIZING
vtx = int(input())
start = 1
for i in range(5):
  star*=(vtx-i)
print(star//120)

# OPTIMIZING
N = int(input())
print(N * (N-1) * (N-2) * (N-3) * (N-4) * (N-5) // 120)
# 과녁 : 1 / 2 / 4 / 8 / 16 / 32 / 64 / 128 / 256 / 512
# 2**0 2**9
# a, b 둘 중 한 명만 맞춘 표적만 맞춤

bi = [0 for _ in range(10)]

def bitmap(n: int):
  for i in range(9, -1, -1):
    if 2**i <= n:
      bi[i] += 1
      n -= 2**i

if __name__ == "__main__":
  a, b = map(int, input().split())
  bitmap(a)
  bitmap(b)

  sol = 0
  for x, y in enumerate(bi):
    if y == 1:
      sol += 2**x
  print(sol)

  # OPTIMIZING
a,b=map(int,input().split())
print(a^b)
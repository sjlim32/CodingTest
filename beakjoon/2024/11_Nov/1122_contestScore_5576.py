
W, K = [], []
for _ in range(10):
  W.append(int(input()))
for _ in range(10):
  K.append(int(input()))

Top_W = sorted(W, reverse=True)
Top_K = sorted(K, reverse=True)
print(sum(Top_W[0:3]), sum(Top_K[0:3]))

# OPTIMIZING
W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]
print(sum(sorted(W)[-3:]), sum(sorted(K)[-3:]))
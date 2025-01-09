# 3
# 2 3 4

# 최대값 인덱스와 최대값을 통해 다음 가장 큰 값과 비교해야함

goal = int(input()) + 1
tree = list(map(int, input().split()))

ans = -1

for i, lemon in enumerate(tree):
  if lemon - (goal - (i + 1)) > ans:
    ans = lemon - (goal - (i + 1))

print(ans)

# OPTIMIZING
n,*l=map(int,open(0).read().split())
print(max(i+j-n for i,j in zip(l,range(n))))

n,*x=map(int,open(0).read().split())
print(max([0]+[i-n+x[i]for i in range(n)]))
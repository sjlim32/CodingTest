foods = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum = 0

for i in range(int(input())):
  foods[i] = int(input())
for _ in range(int(input())):
  k = int(input())
  sum += foods[k - 1] 

print(sum)

# OPTIMIZING
n,*l=map(int,open(0));print(sum(l[i-1]for i in l[n+1:]))
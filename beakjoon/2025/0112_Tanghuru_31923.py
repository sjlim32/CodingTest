
N, P, Q = map(int, input().split())
berry = list(map(int, input().split()))
muscat = list(map(int, input().split()))

answer = []

for i in range(N):
  b = berry[i]
  m = muscat[i]
  min = 0

  while b != m:
    b += P
    m += Q
    min += 1

    if min == 10000:
      print("NO")
      exit()

  answer.append(min)

print("YES")
print(" ".join(map(str, answer)))

# OPTIMIZING
n, p, q=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

num=[]
if p==q: 
    if a==b:
        num=[0 for _ in range(n)]
    else:
        print('NO')
        exit(0)
else:
    for i in range(n):
        k=(a[i]-b[i])/(q-p)
        if k.is_integer() and k>=0:
            num.append(int(k))
        else:
            print('NO')
            exit(0)
print('YES')
print(*num, sep=' ')
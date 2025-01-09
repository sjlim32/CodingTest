n = int(input())
a, b, c = 1, 1, 1

if n == 3:
  a, b, c = map(int, input().split())
  for i in range(1, (min(a, b, c) + 1)):
    if (a % i == 0) and (b % i == 0) and (c % i == 0):
      print(i)
else:
  a, b = map(int, input().split())
  for i in range(1, (min(a, b)+ 1)):
    if (a % i == 0) and (b % i == 0):
      print(i)
  

# OPTIMIZING
N = int(input())
    
def ddd(l,a):
  for i in range(1,int(a**(1/2))+1):
    if a%i == 0:
      l.append(i)
      if (i**2)!=a:
        l.append(a//i)
  l = set(l)
  return l
    
if N == 2:
  a,b = map(int,input().split())
  l1 = []
  l2 = []
  ll = list(ddd(l1,a) & ddd(l2,b))
  ll.sort()
  for i in ll:
    print(i)
    
if N == 3:
  a,b,c = map(int,input().split())
  l1 = []
  l2 = []
  l3 = []
  ll = list(ddd(l1,a) & ddd(l2,b) & ddd(l3,c))
  ll.sort()
  for i in ll:
    print(i)
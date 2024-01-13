# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

n = int(input())  
l = list(map(int, input().split()))
a = 0

for i in l:
  j = 2
  while i > j:          # 
    if i % j == 0:      # 나머지가 없으면 소수 아님 > break
      break;
    else:               # 나머지가 있으면 j를 1씩 높임
      j += 1
  if i != 1 and i == j:
    a += 1                   
print(a)


## Optimizing ##
##### 자신의 제곱근 이하의 수까지만 검사

input()
l = list(map(int, input().split()))
cont = 0

for x in l:
  if x <= 1: continue                         
  for j in range(2, int(x ** 1/2)+1):         # 제곱근 구하는 방법 = x ** 1/2 or math.sqrt(x)
    if x % j == 0: break                      
  else:
    cont += 1
print(cont)

##### 에라토스테네스의 체 -> 임의의 자연수 n 이하의 소수를 모두 검색

def prime_list(n):
  sieve = [True] * (n+1)                  # n개의 True 가 담긴 배열 생성

  m = int(n ** 0.5)                       # 제곱근
  for i in range (2, m + 1):              # 2 부터 제곱근까지의 범위를 반복
    if sieve[i]:                          # sieve[i] 가 소수라면,
      for j in range(i * i, n+1, i):      # sieve[i] 의 모든 배수는 False
        sieve[j] = False

  return [ num for num in range(2, n+1) if sieve[num]]

print(prime_list(30))
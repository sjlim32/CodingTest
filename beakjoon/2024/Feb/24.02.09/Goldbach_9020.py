from itertools import combinations_with_replacement
from collections import defaultdict
import sys
input = sys.stdin.readline

def prime_list(n):
  sieve = [True] * (n+1)                  # n개의 True 가 담긴 배열 생성

  m = int(n ** 0.5)                       # 제곱근
  for i in range (2, m + 1):              # 2 부터 제곱근까지의 범위를 반복
    if sieve[i]:                          # sieve[i] 가 소수라면,
      for j in range(i * i, n+1, i):      # sieve[i] 의 모든 배수는 False
        sieve[j] = False

  return [ num for num in range(2, n+1) if sieve[num]]

if __name__ == "__main__":
  tc = int(input())
  primes = prime_list(10000)
  
  for _ in range(tc):
    n = int(input())

    nplist= []
    for i in range (len(primes)):
      if primes[i] <= n:
        nplist.append(primes[i])
      else:
        break;

    

    # prime_comb = list(combinations_with_replacement(nplist, 2))
    
    # res = defaultdict(int)
    # for a, b in prime_comb:
    #   if a + b == n:
    #     res[b-a] = [a, b]
    # mininum = min(res.keys())
    # print(f"{res[mininum][0]} {res[mininum][1]}")
# from itertools import combinations_with_replacement, combinations
# from collections import defaultdict
import sys
input = sys.stdin.readline
print = sys.stdout.write

def prime_list(n : int) -> list:
  sieve = [True] * (n+1)                  # n개의 True 가 담긴 배열 생성

  m = int(n ** 0.5)                       # 제곱근
  for i in range (2, m + 1):              # 2 부터 제곱근까지의 범위를 반복
    if sieve[i]:                          # sieve[i] 가 소수라면,
      for j in range(i * i, n+1, i):      # sieve[i] 의 모든 배수는 False
        sieve[j] = False
  return [ num for num in range(2, n+1) if sieve[num]]

def find_comb(n: int) -> None:
  half = n // 2

  if half in primes:
    print(f"{half} {half}\n")
  else:
    ph = (n // 2) + 1
    mh = (n // 2) - 1
    while True:
      if mh not in primes:
        mh -= 1
        continue
      if ph not in primes:
        ph += 1
        continue
      
      if mh + ph == n:
        print(f"{mh} {ph}\n")
        return
      elif mh + ph < n:
        ph += 1
      else:
        mh -= 1

if __name__ == "__main__":
  tc = int(input())
  primes = set(prime_list(10000))

  for _ in range(tc):
    n = int(input())
    find_comb(n)

  # for _ in range(tc):
  #   n = int(input())
  #   prime = list(combinations_with_replacement(prime_list(n), 2))
  #   res = defaultdict(int)

  #   for a, b in prime:
  #     if a + b == n:
  #       res[b-a] = [a, b]
  #   mininum = min(res.keys())
  #   print(f"{res[mininum][0]} {res[mininum][1]}")
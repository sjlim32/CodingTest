# n = 6

# dp = [ 0 for _ in range(6) ]

# for i in range(n):
#   dp[i] = [ i for _ in range(n) ]

# print(dp)
# print(max(dp))

# dp2 = [ [0] * n ] * n
# print(dp2)

# 1원, 5원, 10원, 50원, 100원, 500원
# 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능
# 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성

# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
# 첫 번째 줄에는 동전의 가지 수 N(1 ≤ N ≤ 20)이 주어지고 
# 두 번째 줄에는 N가지 동전의 각 금액이 오름차순으로 정렬, 공백으로 구분, 각 금액은 정수로서 1원부터 10000원까지
# N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)

import sys
input = sys.stdin.readline
print = sys.stdout.write

def res(coins: list, types: int, price: int):
  # 동전의 종류는 오름차수 = 1, 5, 10, ...
  
  # outcomes = 0
  # dp = [0] * (n + 1)
  # # for coin in coins:
  # #   123
  # return outcomes

  dp = [0] * (price + 1)
  dp[0] = 1

  for coin in coins:
    for p in range(price + 1):
      dp[p] += dp[p - coin] if p >= coin else 0
      # if p < coin:
      #   continue
      # else:
      #   dp[p] += dp[p - coin]

  return dp[price]

  return dp[price]


if __name__ == "__main__":
  for _ in range(int(input())):
    coin_types = int(input())
    coins = list(map(int, input().split()))
    price = int(input())

    print(f'{res(coins, coin_types, price)}\n')

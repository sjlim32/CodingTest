# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 N개의 줄, Ti와 Pi가 공백으로 구분, 1일부터 N일까지 순서대로 주어진다. 
# 1 ≤ Ti ≤ 5      //    1 ≤ Pi ≤ 1,000




# n = int(input())
# table = [[0, 0]]

# for _ in range(n):
#   t, v = map(int, input().split())
#   table.append([t, v])

# dp = [ [0] * (n + 1) for _ in range(n + 1) ]

# for i in range(1, n):
#   t, v = table[i]

#   if i + t <= n:
#     dp[i][i + t] = max(dp[i - 1][i + t], dp[i - 1][i] + v)

# print(max(dp))

n = int(input())
table = []

for _ in range(n):
  t, v = map(int, input().split())
  table.append([t, v])

dp = [0] * (n + 1)

for i in range(n):
  t, v = table[i]

  if i + t <= n:
    dp[i + t] = max(dp[i - t + 1] + v, dp[i])

print(max(dp))